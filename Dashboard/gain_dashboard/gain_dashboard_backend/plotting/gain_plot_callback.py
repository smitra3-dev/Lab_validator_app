#dashboard/gain/plotting/gain_plot_callback.py
import plotly.graph_objects as go
from dash.dependencies import Input, Output

from ..config.gain_constants import GAIN_GROUP_COLS
from ..config.gain_labels import GAIN_LABEL_MAP
from ..config.gain_plot_style import apply_gain_figure_layout
from ..filters.gain_filter_query import apply_gain_filters
from .gain_plot_data import prepare_gain_plot_dataframe, normalize_selected_params, find_valid_gain_params
from .gain_trace_builder import add_gain_curve_trace
from .gain_error_overlay import add_gain_error_overlays, build_gain_debug_children
from ..validation.gain_validation_runner import run_gain_validation_sections


def register_gain_plot_callback(app, df):
    @app.callback(
        Output("gain-plot", "figure"),
        Output("gain-validation_output", "children"),
        Output("gain-error_output", "children"),
        Output("gain-debug_panel", "children"),
        Input("gain-macro", "value"),
        Input("gain-device", "value"),
        Input("gain-siteX", "value"),
        Input("gain-siteY", "value"),
        Input("gain-vd_select", "value"),
        Input("gain-parameter", "value"),
        Input("gain-error-toggle", "value"),
        Input("gain-xscale", "value"),
        Input("gain-yscale", "value"),
    )
    def update_gain_plot(macro, device, siteX, siteY, vd, params, error_toggle, xscale, yscale):
        error_detection_on = isinstance(error_toggle, list) and ("on" in error_toggle)

        filtered = apply_gain_filters(
            df,
            macro=macro,
            device=device,
            siteX=siteX,
            siteY=siteY,
            vd=vd,
        )

        pdf, error_message = prepare_gain_plot_dataframe(filtered)
        if pdf is None:
            return (
                go.Figure().update_layout(title=error_message),
                "No validation results",
                "No error validation",
                "No debug data",
            )

        params = normalize_selected_params(params)
        if not params:
            return go.Figure(), "Select parameter(s)", "No error validation", "No debug data"

        valid_params = find_valid_gain_params(pdf, params)
        if not valid_params:
            return (
                go.Figure().update_layout(title="Selected parameter not found"),
                "No validation results",
                "No error validation",
                "No debug data",
            )

        grouped_for_count = list(pdf.groupby(GAIN_GROUP_COLS))
        total_curves = len(grouped_for_count) * len(valid_params)
        if total_curves > 80:
            return (
                go.Figure().update_layout(title="Too many curves selected. Reduce filters."),
                "Too many curves selected",
                "Too many curves selected",
                "Too many curves selected",
            )

        fig = go.Figure()
        trend_debug_logs = []

        for param in valid_params:
            for keys, group in pdf.groupby(GAIN_GROUP_COLS):
                group = group.sort_values("Id").copy()

                if xscale == "log":
                    group = group[group["Id"] > 0]
                if yscale == "log":
                    group = group[group[param] > 0]

                if group.empty or len(group) < 2:
                    trend_debug_logs.append(f"[SKIP] {param} | {keys} -> insufficient positive data for selected log scale")
                    continue

                add_gain_curve_trace(fig, group, param, keys)

                if error_detection_on:
                    add_gain_error_overlays(fig, group, param, trend_debug_logs)

        validation_children, ftfmax_children = run_gain_validation_sections(pdf, valid_params)
        debug_children = build_gain_debug_children(error_detection_on, trend_debug_logs)

        merged_validation_children = []
        if isinstance(validation_children, list):
            merged_validation_children.extend(validation_children)
        if isinstance(ftfmax_children, list):
            merged_validation_children.extend(ftfmax_children)

        y_title = ", ".join([GAIN_LABEL_MAP.get(p, p) for p in valid_params])
        fig = apply_gain_figure_layout(fig, valid_params, xscale, yscale, y_title)

        error_children = ["No error criteria triggered"] if error_detection_on else ["Error detection is OFF"]

        return fig, merged_validation_children or ["No validation results"], error_children, debug_children

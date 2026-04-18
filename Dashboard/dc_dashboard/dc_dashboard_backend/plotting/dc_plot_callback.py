##dashboard/dc/plotting/dc_plot_callback.py

import plotly.graph_objects as go
from dash.dependencies import Input, Output

from ..config.dc_constants import DC_GROUP_COLS
from ..config.dc_labels import DC_LABEL_MAP
from ..config.dc_plot_style import apply_dc_figure_layout
from ..filters.dc_filter_query import apply_dc_filters
from .dc_plot_data import prepare_dc_plot_dataframe, normalize_selected_params, find_valid_dc_params
from .dc_trace_builder import add_dc_curve_trace
from .dc_error_overlay import add_dc_error_overlays, build_dc_debug_children
from ..validation.dc_validation_runner import run_dc_validation_sections


def register_dc_plot_callback(app, df):
    @app.callback(
        Output("dc-plot", "figure"),
        Output("dc-validation_output", "children"),
        Output("dc-error_output", "children"),
        Output("dc-debug_panel", "children"),
        Input("dc-macro", "value"),
        Input("dc-device", "value"),
        Input("dc-siteX", "value"),
        Input("dc-siteY", "value"),
        Input("dc-vd_select", "value"),
        Input("dc-parameter", "value"),
        Input("dc-error-toggle", "value"),
        Input("dc-xscale", "value"),
        Input("dc-yscale", "value"),
    )
    def update_dc_plot(macro, device, siteX, siteY, vd, params, error_toggle, xscale, yscale):
        error_detection_on = isinstance(error_toggle, list) and ("on" in error_toggle)

        filtered = apply_dc_filters(
            df,
            macro=macro,
            device=device,
            siteX=siteX,
            siteY=siteY,
            vd=vd,
        )

        pdf, error_message = prepare_dc_plot_dataframe(filtered)
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

        valid_params = find_valid_dc_params(pdf, params)
        if not valid_params:
            return (
                go.Figure().update_layout(title="Selected parameter not found"),
                "No validation results",
                "No error validation",
                "No debug data",
            )

        grouped_for_count = list(pdf.groupby(DC_GROUP_COLS))
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
            for keys, group in pdf.groupby(DC_GROUP_COLS):
                group = group.sort_values("Vg").copy()

                if xscale == "log":
                    group = group[group["Vg"] > 0]
                if yscale == "log":
                    group = group[group[param] > 0]

                if group.empty or len(group) < 2:
                    trend_debug_logs.append(f"[SKIP] {param} | {keys} -> insufficient positive data for selected log scale")
                    continue

                add_dc_curve_trace(fig, group, param, keys)

                if error_detection_on:
                    add_dc_error_overlays(fig, group, param, trend_debug_logs)

        validation_children, cap_children, ftfmax_children = run_dc_validation_sections(pdf, valid_params)
        debug_children = build_dc_debug_children(error_detection_on, trend_debug_logs)

        # keep current 3-panel API by merging cap + ftfmax into validation area if needed
        merged_validation_children = []
        if isinstance(validation_children, list):
            merged_validation_children.extend(validation_children)
        if isinstance(cap_children, list):
            merged_validation_children.extend(cap_children)
        if isinstance(ftfmax_children, list):
            merged_validation_children.extend(ftfmax_children)

        y_title = ", ".join([DC_LABEL_MAP.get(p, p) for p in valid_params])
        fig = apply_dc_figure_layout(fig, valid_params, xscale, yscale, y_title)

        error_children = ["No error criteria triggered"] if error_detection_on else ["Error detection is OFF"]

        return fig, merged_validation_children or ["No validation results"], error_children, debug_children

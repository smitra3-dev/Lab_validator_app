##plotting/rf_plot_callback.py

from dash.dependencies import Input, Output
import plotly.graph_objects as go

from ..config.rf_constants import RF_GROUP_COLS
from ..config.rf_plot_style import apply_rf_figure_layout
from ..filters.rf_filter_query import apply_rf_filters
from .rf_plot_data import prepare_rf_plot_dataframe, find_valid_rf_params, normalize_selected_params
from .rf_trace_builder import add_rf_curve_trace
from .rf_error_overlay import add_rf_error_overlays, build_rf_debug_children
from ..validations.rf_validation_runner import run_rf_validation_sections


def register_rf_plot_callback(app, df):
    @app.callback(
        Output("rf-plot", "figure"),
        Output("rf-validation_output", "children"),
        Output("rf-sparam_output", "children"),
        Output("rf-h21_output", "children"),
        Output("rf-cap_output", "children"),
        Output("rf-ftfmax_output", "children"),
        Output("rf-debug_panel", "children"),
        Input("rf-macro", "value"),
        Input("rf-device", "value"),
        Input("rf-siteX", "value"),
        Input("rf-siteY", "value"),
        Input("rf-Vd", "value"),
        Input("rf-Vg", "value"),
        Input("rf-parameter", "value"),
        Input("rf-xscale", "value"),
        Input("rf-yscale", "value"),
        Input("rf-error-toggle", "value"),
    )
    def update_rf_plot(macro, device, siteX, siteY, vd, vg, params, xscale, yscale, error_toggle):
        error_detection_on = isinstance(error_toggle, list) and ("on" in error_toggle)

        filtered = apply_rf_filters(
            df,
            macro=macro,
            device=device,
            siteX=siteX,
            siteY=siteY,
            vd=vd,
            vg=vg,
        )

        pdf, error_message = prepare_rf_plot_dataframe(filtered)
        if pdf is None:
            return (
                go.Figure().update_layout(title=error_message),
                "No data to validate",
                "No S-parameter validation",
                "No h21 validation",
                "No capacitance validation",
                "No Ft/Fmax validation",
                "No debug data",
            )

        params = normalize_selected_params(params)
        if not params:
            return (
                go.Figure(),
                "Select parameter(s)",
                "No S-param",
                "No h21",
                "No capacitance validation",
                "No Ft/Fmax validation",
                "No debug",
            )

        valid_params = find_valid_rf_params(pdf, params)
        if not valid_params:
            return (
                go.Figure().update_layout(title="Selected parameter(s) not found"),
                "No validation results",
                "No S-parameter validation",
                "No h21 validation",
                "No capacitance validation",
                "No Ft/Fmax validation",
                "No debug data",
            )

        grouped_for_count = list(pdf.groupby(RF_GROUP_COLS))
        total_curves = len(grouped_for_count) * len(valid_params)
        if total_curves > 120:
            return (
                go.Figure().update_layout(title="Too many curves selected. Reduce filters."),
                "Too many curves selected",
                "Too many curves selected",
                "Too many curves selected",
                "Too many curves selected",
                "Too many curves selected",
                "Too many curves selected",
            )

        fig = go.Figure()
        trend_debug_logs = []

        for param in valid_params:
            for keys, group in pdf.groupby(RF_GROUP_COLS):
                group = group.sort_values("Fs").copy()

                if xscale == "log":
                    group = group[group["Fs"] > 0]
                if yscale == "log":
                    group = group[group[param] > 0]

                if group.empty or len(group) < 2:
                    trend_debug_logs.append(
                        f"[SKIP] {param} | {keys} -> insufficient positive data for selected log scale"
                    )
                    continue

                add_rf_curve_trace(fig, group, param, keys)

                if error_detection_on:
                    add_rf_error_overlays(fig, group, param, trend_debug_logs)

        debug_children = build_rf_debug_children(error_detection_on, trend_debug_logs)

        validation_children, sparam_children, h21_children, cap_children, ftfmax_children = (
            run_rf_validation_sections(pdf, valid_params, xscale, yscale)
        )

        fig = apply_rf_figure_layout(fig, valid_params, xscale, yscale)

        return (
            fig,
            validation_children,
            sparam_children,
            h21_children,
            cap_children,
            ftfmax_children,
            debug_children,
        )

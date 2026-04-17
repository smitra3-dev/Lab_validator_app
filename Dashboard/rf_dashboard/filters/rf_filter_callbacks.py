##filters/rf_filter_callbacks.py

from dash.dependencies import Input, Output
import polars as pl

from .filter_utils import to_list, make_options, keep_valid
from .rf_filter_query import collect_unique


def register_rf_filter_callbacks(app, df):
    @app.callback(
        Output("rf-device", "options"),
        Output("rf-device", "value"),
        Input("rf-macro", "value"),
        Input("rf-device", "value"),
    )
    def update_rf_device_options(macro, current_device):
        macro = to_list(macro)
        if not macro:
            return [], []

        filtered = df.filter(pl.col("macro").is_in(macro))
        values = collect_unique(filtered, "device")
        return make_options(values), keep_valid(current_device, values)

    @app.callback(
        Output("rf-siteX", "options"),
        Output("rf-siteX", "value"),
        Input("rf-macro", "value"),
        Input("rf-device", "value"),
        Input("rf-siteX", "value"),
    )
    def update_rf_sitex_options(macro, device, current_sitex):
        macro = to_list(macro)
        device = to_list(device)

        if not macro:
            return [], []

        filtered = df.filter(pl.col("macro").is_in(macro))
        if device:
            filtered = filtered.filter(pl.col("device").is_in(device))

        values = collect_unique(filtered, "siteX")
        return make_options(values), keep_valid(current_sitex, values)

    @app.callback(
        Output("rf-siteY", "options"),
        Output("rf-siteY", "value"),
        Input("rf-macro", "value"),
        Input("rf-device", "value"),
        Input("rf-siteX", "value"),
        Input("rf-siteY", "value"),
    )
    def update_rf_sitey_options(macro, device, siteX, current_sitey):
        macro = to_list(macro)
        device = to_list(device)
        siteX = to_list(siteX)

        if not macro:
            return [], []

        filtered = df.filter(pl.col("macro").is_in(macro))
        if device:
            filtered = filtered.filter(pl.col("device").is_in(device))
        if siteX:
            filtered = filtered.filter(pl.col("siteX").is_in(siteX))

        values = collect_unique(filtered, "siteY")
        return make_options(values), keep_valid(current_sitey, values)

    @app.callback(
        Output("rf-Vd", "options"),
        Output("rf-Vd", "value"),
        Input("rf-macro", "value"),
        Input("rf-device", "value"),
        Input("rf-siteX", "value"),
        Input("rf-siteY", "value"),
        Input("rf-Vd", "value"),
    )
    def update_rf_vd_options(macro, device, siteX, siteY, current_vd):
        macro = to_list(macro)
        device = to_list(device)
        siteX = to_list(siteX)
        siteY = to_list(siteY)

        if not macro:
            return [], []

        filtered = df.filter(pl.col("macro").is_in(macro))
        if device:
            filtered = filtered.filter(pl.col("device").is_in(device))
        if siteX:
            filtered = filtered.filter(pl.col("siteX").is_in(siteX))
        if siteY:
            filtered = filtered.filter(pl.col("siteY").is_in(siteY))

        values = collect_unique(filtered, "Vd")
        return make_options(values), keep_valid(current_vd, values)

    @app.callback(
        Output("rf-Vg", "options"),
        Output("rf-Vg", "value"),
        Input("rf-macro", "value"),
        Input("rf-device", "value"),
        Input("rf-siteX", "value"),
        Input("rf-siteY", "value"),
        Input("rf-Vd", "value"),
        Input("rf-Vg", "value"),
    )
    def update_rf_vg_options(macro, device, siteX, siteY, vd, current_vg):
        macro = to_list(macro)
        device = to_list(device)
        siteX = to_list(siteX)
        siteY = to_list(siteY)
        vd = to_list(vd)

        if not macro:
            return [], []

        filtered = df.filter(pl.col("macro").is_in(macro))
        if device:
            filtered = filtered.filter(pl.col("device").is_in(device))
        if siteX:
            filtered = filtered.filter(pl.col("siteX").is_in(siteX))
        if siteY:
            filtered = filtered.filter(pl.col("siteY").is_in(siteY))
        if vd:
            filtered = filtered.filter(pl.col("Vd").is_in(vd))

        values = collect_unique(filtered, "Vg")
        return make_options(values), keep_valid(current_vg, values)


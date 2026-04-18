##dashboard/dc/filters/dc_filter_callbacks.py

from dash.dependencies import Input, Output
import polars as pl

from .filter_utils import to_list, make_options, keep_valid
from .dc_filter_query import collect_unique


def register_dc_filter_callbacks(app, df):
    @app.callback(
        Output("dc-device", "options"),
        Output("dc-device", "value"),
        Input("dc-macro", "value"),
        Input("dc-device", "value"),
    )
    def update_dc_device_options(macro, current_device):
        macro = to_list(macro)
        if not macro:
            return [], []

        filtered = df.filter(pl.col("macro").is_in(macro))
        values = collect_unique(filtered, "device")
        return make_options(values), keep_valid(current_device, values)

    @app.callback(
        Output("dc-siteX", "options"),
        Output("dc-siteX", "value"),
        Input("dc-macro", "value"),
        Input("dc-device", "value"),
        Input("dc-siteX", "value"),
    )
    def update_dc_sitex_options(macro, device, current_sitex):
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
        Output("dc-siteY", "options"),
        Output("dc-siteY", "value"),
        Input("dc-macro", "value"),
        Input("dc-device", "value"),
        Input("dc-siteX", "value"),
        Input("dc-siteY", "value"),
    )
    def update_dc_sitey_options(macro, device, siteX, current_sitey):
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
        Output("dc-vd_select", "options"),
        Output("dc-vd_select", "value"),
        Input("dc-macro", "value"),
        Input("dc-device", "value"),
        Input("dc-siteX", "value"),
        Input("dc-siteY", "value"),
        Input("dc-vd_select", "value"),
    )
    def update_dc_vd_options(macro, device, siteX, siteY, current_vd):
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

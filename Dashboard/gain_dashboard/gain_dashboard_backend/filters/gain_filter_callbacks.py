#dashboard/gain/filters/gain_filter_callbacks.py

import polars as pl
from dash import Input, Output


def _to_list(value):
    if value is None:
        return []
    if isinstance(value, list):
        return [v for v in value if v is not None and v != ""]
    return [value]


def _make_options(values):
    return [{"label": str(v), "value": v} for v in values]


def _keep_valid(selected, valid_values):
    selected_list = _to_list(selected)
    valid_set = set(valid_values)
    return [v for v in selected_list if v in valid_set]


def _collect_unique(filtered, col_name):
    query = filtered.select(col_name).drop_nulls().unique()
    series = query.collect()[col_name] if isinstance(query, pl.LazyFrame) else query[col_name]
    values = [v for v in series.to_list() if v is not None]
    return sorted(values, key=lambda x: str(x))


def register_gain_filter_callbacks(app, df):
    @app.callback(
        Output("gain-device", "options"),
        Output("gain-device", "value"),
        Input("gain-macro", "value"),
        Input("gain-device", "value"),
    )
    def update_gain_device_options(macro, current_device):
        macro = _to_list(macro)
        if not macro:
            return [], []

        filtered = df.filter(pl.col("macro").is_in(macro))
        values = _collect_unique(filtered, "device")
        return _make_options(values), _keep_valid(current_device, values)

    @app.callback(
        Output("gain-siteX", "options"),
        Output("gain-siteX", "value"),
        Input("gain-macro", "value"),
        Input("gain-device", "value"),
        Input("gain-siteX", "value"),
    )
    def update_gain_sitex_options(macro, device, current_sitex):
        macro = _to_list(macro)
        device = _to_list(device)
        if not macro:
            return [], []

        filtered = df.filter(pl.col("macro").is_in(macro))
        if device:
            filtered = filtered.filter(pl.col("device").is_in(device))

        values = _collect_unique(filtered, "siteX")
        return _make_options(values), _keep_valid(current_sitex, values)

    @app.callback(
        Output("gain-siteY", "options"),
        Output("gain-siteY", "value"),
        Input("gain-macro", "value"),
        Input("gain-device", "value"),
        Input("gain-siteX", "value"),
        Input("gain-siteY", "value"),
    )
    def update_gain_sitey_options(macro, device, siteX, current_sitey):
        macro = _to_list(macro)
        device = _to_list(device)
        siteX = _to_list(siteX)
        if not macro:
            return [], []

        filtered = df.filter(pl.col("macro").is_in(macro))
        if device:
            filtered = filtered.filter(pl.col("device").is_in(device))
        if siteX:
            filtered = filtered.filter(pl.col("siteX").is_in(siteX))

        values = _collect_unique(filtered, "siteY")
        return _make_options(values), _keep_valid(current_sitey, values)

    @app.callback(
        Output("gain-vd_select", "options"),
        Output("gain-vd_select", "value"),
        Input("gain-macro", "value"),
        Input("gain-device", "value"),
        Input("gain-siteX", "value"),
        Input("gain-siteY", "value"),
        Input("gain-vd_select", "value"),
    )
    def update_gain_vd_options(macro, device, siteX, siteY, current_vd):
        macro = _to_list(macro)
        device = _to_list(device)
        siteX = _to_list(siteX)
        siteY = _to_list(siteY)
        if not macro:
            return [], []

        filtered = df.filter(pl.col("macro").is_in(macro))
        if device:
            filtered = filtered.filter(pl.col("device").is_in(device))
        if siteX:
            filtered = filtered.filter(pl.col("siteX").is_in(siteX))
        if siteY:
            filtered = filtered.filter(pl.col("siteY").is_in(siteY))

        values = _collect_unique(filtered, "Vd")
        return _make_options(values), _keep_valid(current_vd, values)

    @app.callback(
        Output("gain-parameter", "options"),
        Output("gain-parameter", "value"),
        Input("gain-macro", "value"),
        Input("gain-device", "value"),
        Input("gain-siteX", "value"),
        Input("gain-siteY", "value"),
        Input("gain-vd_select", "value"),
    )
    def update_gain_parameters(macro, device, siteX, siteY, vd):
        macro = _to_list(macro)
        device = _to_list(device)
        siteX = _to_list(siteX)
        siteY = _to_list(siteY)
        vd = _to_list(vd)

        filtered = df
        if macro:
            filtered = filtered.filter(pl.col("macro").is_in(macro))
        if device:
            filtered = filtered.filter(pl.col("device").is_in(device))
        if siteX:
            filtered = filtered.filter(pl.col("siteX").is_in(siteX))
        if siteY:
            filtered = filtered.filter(pl.col("siteY").is_in(siteY))
        if vd:
            filtered = filtered.filter(pl.col("Vd").is_in(vd))

        schema_names = filtered.collect_schema().names() if isinstance(filtered, pl.LazyFrame) else filtered.columns

        exclude_cols = {"technology", "wafer", "macro", "device", "siteX", "siteY", "Vd", "Vg", "Id", "Fs"}
        param_cols = [c for c in schema_names if c not in exclude_cols]

        preferred_order = [
            "Ft_mean", "Fmax_mean", "gm", "gds", "Ig",
            "Cgs", "Cgd", "Cgg",
            "h21_mag", "h21_dB",
            "S11", "S12", "S21", "S22",
            "S11_dB", "S12_dB", "S21_dB", "S22_dB",
            "Y11_mag", "Y12_mag", "Y21_mag", "Y22_mag",
            "Y11_dB", "Y12_dB", "Y21_dB", "Y22_dB",
        ]

        ordered = [c for c in preferred_order if c in param_cols]
        ordered.extend(sorted([c for c in param_cols if c not in ordered]))

        options = [{"label": c, "value": c} for c in ordered]
        default_value = [c for c in ["gm"] if c in ordered]
        if not default_value and ordered:
            default_value = [ordered[0]]

        return options, default_value
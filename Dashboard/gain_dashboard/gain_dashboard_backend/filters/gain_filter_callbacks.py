#dashboard/gain/filters/gain_filter_callbacks.py

import polars as pl
from dash.dependencies import Input, Output


def register_gain_filter_callbacks(app, df):
    @app.callback(
        Output("gain-device", "options"),
        Input("gain-macro", "value"),
    )
    def update_gain_device(macro):
        if not macro:
            return []

        filtered = df.filter(pl.col("macro").is_in(macro))
        pdf = filtered.select(["macro", "device"]).unique().collect().to_pandas()

        result = []
        for m in macro:
            devs = pdf[pdf["macro"] == m]["device"].dropna().unique()
            for d in devs:
                result.append({"label": f"{m} | {d}", "value": d})
        return result

    @app.callback(
        Output("gain-siteX", "options"),
        Input("gain-macro", "value"),
    )
    def update_gain_siteX(macro):
        if not macro:
            return []

        values = (
            df.filter(pl.col("macro").is_in(macro))
            .select("siteX").unique().collect()["siteX"].to_list()
        )
        values = [v for v in values if v is not None]
        return [{"label": str(v), "value": v} for v in sorted(values)]

    @app.callback(
        Output("gain-siteY", "options"),
        Input("gain-macro", "value"),
        Input("gain-siteX", "value"),
    )
    def update_gain_siteY(macro, siteX):
        if not macro:
            return []

        filtered = df.filter(pl.col("macro").is_in(macro))
        if siteX:
            filtered = filtered.filter(pl.col("siteX").is_in(siteX))

        values = filtered.select("siteY").unique().collect()["siteY"].to_list()
        values = [v for v in values if v is not None]
        return [{"label": str(v), "value": v} for v in sorted(values)]

    @app.callback(
        Output("gain-vd_select", "options"),
        Input("gain-macro", "value"),
        Input("gain-device", "value"),
        Input("gain-siteX", "value"),
        Input("gain-siteY", "value"),
    )
    def update_gain_vd(macro, device, siteX, siteY):
        filtered = df
        if macro:
            filtered = filtered.filter(pl.col("macro").is_in(macro))
        if device:
            filtered = filtered.filter(pl.col("device").is_in(device))
        if siteX:
            filtered = filtered.filter(pl.col("siteX").is_in(siteX))
        if siteY:
            filtered = filtered.filter(pl.col("siteY").is_in(siteY))

        values = filtered.select("Vd").unique().sort("Vd").collect()["Vd"].to_list()
        values = [v for v in values if v is not None]
        return [{"label": str(v), "value": v} for v in values]

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

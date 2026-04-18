#dashboard/gain/filters/gain_filter_query.py

import polars as pl


def apply_gain_filters(df, macro=None, device=None, siteX=None, siteY=None, vd=None):
    filtered = df.clone() if isinstance(df, pl.LazyFrame) else df

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

    return filtered

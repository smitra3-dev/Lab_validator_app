##filters/rf_filter_query.py

import polars as pl

from .filter_utils import to_list


def collect_unique(df, col_name):
    pdf = (
        df.select(col_name)
        .drop_nulls()
        .unique()
        .collect()
        .to_pandas()
    )

    if pdf.empty:
        return []

    values = pdf[col_name].tolist()
    return sorted(values, key=lambda x: str(x))


def apply_rf_filters(df, macro=None, device=None, siteX=None, siteY=None, vd=None, vg=None):
    macro = to_list(macro)
    device = to_list(device)
    siteX = to_list(siteX)
    siteY = to_list(siteY)
    vd = to_list(vd)
    vg = to_list(vg)

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
    if vg:
        filtered = filtered.filter(pl.col("Vg").is_in(vg))

    return filtered

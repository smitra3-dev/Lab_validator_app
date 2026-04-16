from rf_core.rf_column_identifiers.rf_constants import RF_USA_FALLBACK_RENAME_MAP
from rf_core.rf_helper.rf_column_utils import clean_column_names, first_existing_column
from rf_core.rf_helper.rf_numeric_utils import safe_numeric
from rf_core.rf_helper.rf_string_extractors import extract_value_from_keystring


#Updated 13/4/26 subfolder access

def normalize_usa_rf_columns(df):
    out = clean_column_names(df)

    loopbias_col = first_existing(out, ["loopBias", "LoopBias", "loopbias"])
    loophead_col = first_existing(out, ["loopHeadConstants", "LoopHeadConstants", "loopheadconstants"])

    if loopbias_col is not None and ("Vg" not in out.columns or out["Vg"].isna().all()):
        out["Vg"] = extract_value_from_keystring(out[loopbias_col], "Vg")

    if loophead_col is not None and ("Vd" not in out.columns or out["Vd"].isna().all()):
        out["Vd"] = extract_value_from_keystring(out[loophead_col], "Vd")

    existing_map = {k: v for k, v in RF_USA_FALLBACK_RENAME_MAP.items() if k in out.columns}
    out = out.rename(columns=existing_map)

    for col in ["Vd", "Vg", "Fs", "Id", "Ig"]:
        if col in out.columns:
            out[col] = safe_numeric(out[col])

    return out

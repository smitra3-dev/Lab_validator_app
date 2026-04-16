from rf_core.rf_column_identifiers.rf_constants import RF_SINGAPORE_RENAME_MAP
from rf_core.rf_helper.rf_column_utils import clean_column_names
from rf_core.rf_helper.rf_numeric_utils import safe_numeric


#updated 13/4/26 subfolder access

def normalize_singapore_rf_columns(df):
    out = clean_column_names(df)

    existing_map = {k: v for k, v in RF_SINGAPORE_RENAME_MAP.items() if k in out.columns}
    out = out.rename(columns=existing_map)

    for col in ["Vd", "Vg", "Fs", "Id", "Ig"]:
        if col in out.columns:
            out[col] = safe_numeric(out[col])

    return out

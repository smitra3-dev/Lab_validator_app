from rf_core.rf_column_identifiers.rf_constants import (
    RF_REQUIRED_BASE_COLS,
    RF_REQUIRED_SPARAM_COLS,
    RF_NUMERIC_BASE_COLS,
)
from rf_core.rf_helper.rf_column_utils import clean_column_names
from rf_core.rf_helper.rf_schema_utils import ensure_required_columns
from rf_core.rf_helper.rf_numeric_utils import safe_numeric


def prepare_rf_input_schema(df):
    df = clean_column_names(df)
    df = ensure_required_columns(df, RF_REQUIRED_BASE_COLS + RF_REQUIRED_SPARAM_COLS)

    numeric_cols = RF_NUMERIC_BASE_COLS + RF_REQUIRED_SPARAM_COLS
    for col in numeric_cols:
        df[col] = safe_numeric(df[col])

    return df

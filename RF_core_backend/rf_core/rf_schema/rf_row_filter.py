from rf_core.rf_column_identifiers.rf_constants import RF_REQUIRED_SPARAM_COLS

def get_valid_rf_calculation_mask(df):
    return (
        df["Fs"].notna() &
        (df["Fs"] > 0) &
        df[RF_REQUIRED_SPARAM_COLS].notna().all(axis=1)
    )

import pandas as pd


def standardize_numeric_schema(df):
    """
    Force important numeric columns to Float64 so parquet schema
    stays consistent across all sheets and folders.
    """
    df = df.copy()

    float_cols = [
        "siteX", "siteY",
        "Vd", "Vg", "Id", "Ig", "Fs",
        "S11", "S12", "S21", "S22",
        "S11_dB", "S12_dB", "S21_dB", "S22_dB",
        "Y11_mag", "Y12_mag", "Y21_mag", "Y22_mag",
        "Y11_dB", "Y12_dB", "Y21_dB", "Y22_dB",
        "h21_mag", "h21_dB",
        "K_factor", "MSG", "MAG",
        "Ft", "Fmax", "Ft_mean", "Fmax_mean",
        "gm", "gds",
        "Cgs", "Cgd", "Cgg",
    ]

    for col in float_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce").astype("float64")

    return df

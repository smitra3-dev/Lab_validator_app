def build_rf_base_result(df):
    return df[
        [
            "technology", "wafer", "macro", "device",
            "siteX", "siteY", "Vd", "Vg", "Id", "Ig", "Fs"
        ]
    ].copy()

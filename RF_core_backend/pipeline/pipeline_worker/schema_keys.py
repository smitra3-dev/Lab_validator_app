def get_identity_cols(df):
    preferred = [
        "technology",
        "wafer",
        "macro",
        "device",
        "siteX",
        "siteY",
        "Vd",
        "Vg",
        "Fs",
    ]
    return [c for c in preferred if c in df.columns]


def get_curve_group_cols(df):
    preferred = [
        "technology",
        "wafer",
        "macro",
        "device",
        "siteX",
        "siteY",
        "Vd",
        "Vg",
    ]
    return [c for c in preferred if c in df.columns]

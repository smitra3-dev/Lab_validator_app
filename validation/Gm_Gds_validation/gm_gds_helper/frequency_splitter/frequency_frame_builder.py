import pandas as pd


def prepare_frequency_dataframe(df, fs_col):
    """
    Build a clean dataframe with internal numeric frequency column '__fs__'.
    """
    if fs_col not in df.columns:
        return None

    fs = pd.to_numeric(df[fs_col], errors="coerce")
    out = df.assign(__fs__=fs).dropna(subset=["__fs__"])

    if len(out) == 0:
        return None

    return out

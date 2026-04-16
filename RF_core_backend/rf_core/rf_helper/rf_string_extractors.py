import re
import pandas as pd


def extract_value_from_keystring(series: pd.Series, key: str) -> pd.Series:
    pattern = rf"{re.escape(key)}\s*=\s*([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?)"
    extracted = series.astype(str).str.extract(pattern, expand=False)
    return pd.to_numeric(extracted, errors="coerce")

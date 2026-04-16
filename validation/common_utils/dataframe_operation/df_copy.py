import pandas as pd


def to_pandas(group):
    if isinstance(group, pd.DataFrame):
        return group.copy()

    try:
        return group.to_pandas()
    except Exception:
        return pd.DataFrame(group)

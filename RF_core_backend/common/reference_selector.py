import pandas as pd


def select_closest_rows(df, group_cols, source_col, target_col, diff_col="ref_diff"):
    if source_col not in df.columns or target_col not in df.columns:
        return pd.DataFrame(columns=list(df.columns))

    working_df = df.copy()
    working_df[diff_col] = (working_df[source_col] - working_df[target_col]).abs()

    valid_df = working_df[working_df[diff_col].notna()].copy()
    if valid_df.empty:
        return pd.DataFrame(columns=list(df.columns))

    selected_parts = []

    for _, g in valid_df.groupby(group_cols, dropna=False):
        if g.empty or g[diff_col].isna().all():
            continue

        idx = g[diff_col].idxmin()
        selected_parts.append(g.loc[[idx]])

    if not selected_parts:
        return pd.DataFrame(columns=list(df.columns))

    return pd.concat(selected_parts, ignore_index=True)

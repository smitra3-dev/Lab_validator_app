import pandas as pd


def merge_dc_reference(primary_df, gain_df, group_cols):
    return pd.merge(
        primary_df,
        gain_df[group_cols + ["Ft_mean"]],
        on=group_cols,
        how="inner",
    )

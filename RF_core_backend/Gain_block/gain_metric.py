def compute_gain_means(df, group_cols):
    bias_mean = (
        df.groupby(group_cols, dropna=False)[["Ft", "Fmax"]]
        .mean()
        .reset_index()
        .rename(columns={"Ft": "Ft_mean", "Fmax": "Fmax_mean"})
    )
    return bias_mean

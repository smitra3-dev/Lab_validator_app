def check_fs_sweep_consistency(df, group_cols):
    if not group_cols or "Fs" not in df.columns:
        return

    counts = df.groupby(group_cols, dropna=False)["Fs"].nunique()

    if len(counts) > 0:
        if counts.nunique() > 1:
            print("WARNING: Fs sweep inconsistency detected")
            print(f"Unique Fs counts per curve: {sorted(counts.unique().tolist())}")
        else:
            print(f"Fs sweep consistent: {counts.iloc[0]} points per curve")

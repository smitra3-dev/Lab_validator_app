from common.column_builder import build_final_columns


def format_dc_output(df, group_cols, preferred_cols, exclude_cols):
    available = [c for c in preferred_cols if c in df.columns and c not in exclude_cols]

    leading = []
    leading.extend([c for c in ["technology"] if c in df.columns])
    leading.extend([c for c in group_cols if c in df.columns])
    leading.append("Ft_mean")

    final_cols = build_final_columns(df, leading, available, exclude_cols, skip_cols={"Fs"})

    final_df = df[final_cols].copy()

    sort_cols = [c for c in ["macro", "device", "siteX", "siteY", "Vd", "Vg"] if c in final_df.columns]
    if sort_cols:
        final_df = final_df.sort_values(sort_cols).reset_index(drop=True)

    return final_df

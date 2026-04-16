def build_final_columns(selected_df, leading_cols, preferred_cols, exclude_cols, skip_cols=None):
    skip_cols = set(skip_cols or [])
    exclude_cols = set(exclude_cols)

    protected = set(leading_cols + preferred_cols)
    extra_cols = []

    for col in selected_df.columns:
        if col in protected or col in exclude_cols or col in skip_cols:
            continue
        extra_cols.append(col)

    final_cols = []
    final_cols.extend([c for c in leading_cols if c in selected_df.columns])
    final_cols.extend([c for c in preferred_cols if c in selected_df.columns and c not in final_cols])
    final_cols.extend([c for c in extra_cols if c not in final_cols])

    return final_cols

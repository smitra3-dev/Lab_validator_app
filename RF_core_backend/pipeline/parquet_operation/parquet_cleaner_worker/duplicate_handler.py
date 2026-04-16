def remove_exact_duplicates(df, identity_cols):
    df = df.copy()

    if identity_cols:
        dup_count = df.duplicated(subset=identity_cols).sum()

        if dup_count > 0:
            print(f"WARNING: {dup_count} exact duplicate rows found → removing")
            df = df.drop_duplicates(subset=identity_cols, keep="first")
        else:
            print("No exact structural duplicates found")

    return df

def drop_nan_key_rows(df, key_cols):
    df = df.copy()

    if key_cols:
        before = len(df)
        df = df.dropna(subset=key_cols)
        after = len(df)

        if before != after:
            print(f"Removed {before - after} NaN rows")

    return df

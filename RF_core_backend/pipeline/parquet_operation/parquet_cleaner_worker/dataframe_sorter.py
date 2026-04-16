def sort_structured_dataframe(df, sort_cols):
    df = df.copy()

    if sort_cols:
        df = df.sort_values(by=sort_cols).reset_index(drop=True)
        print(f"Structured & sorted using: {sort_cols}")

    return df

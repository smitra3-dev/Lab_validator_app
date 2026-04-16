from pipeline.parquet_operation.parquet_complex_handler.complex_network_columns import TRUE_COMPLEX_NETWORK_COLUMNS


def drop_true_complex_network_columns(df):
    df = df.copy()

    existing_cols = [col for col in TRUE_COMPLEX_NETWORK_COLUMNS if col in df.columns]

    if existing_cols:
        print(f"Dropping true complex network columns: {existing_cols}")
        df = df.drop(columns=existing_cols)

    return df

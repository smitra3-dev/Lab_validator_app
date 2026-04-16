from pipeline.parquet_operation.parquet_complex_handler.complex_cleaner import clean_complex_columns
from pipeline.parquet_operation.parquet_cleaner_worker.nan_row_handler import drop_nan_key_rows
from pipeline.parquet_operation.parquet_cleaner_worker.duplicate_handler import remove_exact_duplicates
from pipeline.parquet_operation.parquet_cleaner_worker.dataframe_sorter import sort_structured_dataframe

#updated check import 14/04/26

def clean_parquet_dataframe(df, key_cols, identity_cols, sort_cols):
    df = clean_complex_columns(df)
    df = drop_nan_key_rows(df, key_cols)

    if df.empty:
        return df

    df = remove_exact_duplicates(df, identity_cols)
    df = sort_structured_dataframe(df, sort_cols)

    return df

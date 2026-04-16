import os
import re

from pipeline.pipeline_worker.schema_keys import get_identity_cols, get_curve_group_cols
from pipeline.pipeline_worker.schema_standardizer import standardize_numeric_schema
from pipeline.parquet_operation.parquet_complex_handler.complex_cleaner import clean_complex_columns
from pipeline.parquet_operation.parquet_cleaner_worker.nan_row_handler import drop_nan_key_rows
from pipeline.parquet_operation.parquet_cleaner_worker.dataframe_sorter import sort_structured_dataframe
from pipeline.parquet_operation.parquet_cleaner_worker.duplicate_handler import remove_exact_duplicates

from pipeline.parquet_operation.parquet_validator.sweep_validator import check_fs_sweep_consistency

#updated 14/04/26

def save_parquet_dict(data_dict, folder_name):
    os.makedirs(folder_name, exist_ok=True)

    for sheet, df in data_dict.items():
        print(f"\nProcessing save for sheet: {sheet}")

        df = df.copy()

        if df.empty:
            print(f"Skipping empty dataframe for sheet: {sheet}")
            continue

        df = clean_complex_columns(df)
        df = standardize_numeric_schema(df)

        key_cols = [c for c in ["Vg", "Vd", "Fs"] if c in df.columns]
        df = drop_nan_key_rows(df, key_cols)

        if df.empty:
            print(f"Skipping save after cleanup because dataframe became empty: {sheet}")
            continue

        identity_cols = get_identity_cols(df)
        df = remove_exact_duplicates(df, identity_cols)

        sort_cols = [
            c for c in [
                "technology", "wafer", "macro", "device", "siteX", "siteY", "Vd", "Vg", "Fs"
            ]
            if c in df.columns
        ]
        df = sort_structured_dataframe(df, sort_cols)

        group_cols = get_curve_group_cols(df)
        check_fs_sweep_consistency(df, group_cols)

        safe_name = re.sub(r'[\\/*?:"<>|]', "_", sheet)
        file_path = os.path.join(folder_name, f"{safe_name}.parquet")

        df.to_parquet(file_path, index=False)
        print(f"Saved: {file_path}")

    print(f"\nSaved → {folder_name}/ ({len(data_dict)} files)")

#data/parquet_loader.py
import os
import glob
import polars as pl


def load_parquet_folder(folder_path):
    if not folder_path or not os.path.isdir(folder_path):
        return None, None

    parquet_files = glob.glob(os.path.join(folder_path, "*.parquet"))
    if not parquet_files:
        return None, None

    df = pl.scan_parquet(parquet_files)
    meta = pl.read_parquet(parquet_files)

    return df, meta


def load_gain_parquet_folders(gain_folders):
    files = []
    for folder in gain_folders:
        parquet_files = glob.glob(os.path.join(folder, "*.parquet"))
        files.extend(parquet_files)

    if not files:
        return None, None

    df = pl.scan_parquet(files)
    meta = pl.read_parquet(files)

    return df, meta

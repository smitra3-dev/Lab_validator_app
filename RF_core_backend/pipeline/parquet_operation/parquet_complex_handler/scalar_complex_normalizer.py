from pipeline.parquet_operation.parquet_complex_handler.complex_scalar_columns import SCALAR_COMPLEX_CANDIDATES
from pipeline.parquet_operation.parquet_complex_handler.complex_dtype_checker import is_complex_series
from pipeline.parquet_operation.parquet_complex_handler.imaginary_part_checker import get_max_imaginary_part
from pipeline.parquet_operation.parquet_complex_handler.complex_to_real_converter import (
    convert_complex_series_to_real,
    convert_complex_series_to_magnitude,
)


def normalize_scalar_complex_columns(df, imag_tolerance=1e-12):
    df = df.copy()

    for col in SCALAR_COMPLEX_CANDIDATES:
        if col not in df.columns:
            continue

        series = df[col]

        if not is_complex_series(series):
            continue

        max_imag = get_max_imaginary_part(series)

        if max_imag < imag_tolerance:
            print(f"Converting scalar complex column to real: {col}")
            df[col] = convert_complex_series_to_real(series)
        else:
            print(f"Converting scalar complex column to magnitude: {col}")
            df[col] = convert_complex_series_to_magnitude(series)

    return df

from pipeline.parquet_operation.parquet_complex_handler.scalar_complex_normalizer import normalize_scalar_complex_columns
from pipeline.parquet_operation.parquet_complex_handler.complex_network_dropper import drop_true_complex_network_columns

def clean_complex_columns(df, imag_tolerance=1e-12):
    df = normalize_scalar_complex_columns(df, imag_tolerance=imag_tolerance)
    df = drop_true_complex_network_columns(df)
    return df

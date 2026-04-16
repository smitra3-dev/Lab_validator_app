import numpy as np


def convert_complex_series_to_real(series):
    return np.real(series.to_numpy()).astype("float64")


def convert_complex_series_to_magnitude(series):
    return np.abs(series.to_numpy()).astype("float64")

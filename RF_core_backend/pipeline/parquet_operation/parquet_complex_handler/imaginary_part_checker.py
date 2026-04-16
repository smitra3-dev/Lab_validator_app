import numpy as np


def get_max_imaginary_part(series):
    values = series.to_numpy()
    imag_part = np.abs(np.imag(values))

    if len(imag_part) == 0:
        return 0.0

    max_imag = np.nanmax(imag_part)

    if np.isnan(max_imag):
        return 0.0

    return float(max_imag)

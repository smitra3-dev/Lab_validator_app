#validation/common/scaling.py
def normalized_change(y_start, y_end, eps=1e-18):
    denom = max(abs(y_start), abs(y_end), eps)
    return float((y_end - y_start) / denom)


def relative_variation(y, eps=1e-18):
    import numpy as np

    y = np.asarray(y, dtype=float)
    y = y[np.isfinite(y)]

    if len(y) < 2:
        return np.nan

    denom = max(np.nanmedian(np.abs(y)), eps)
    return float((np.nanmax(y) - np.nanmin(y)) / denom)

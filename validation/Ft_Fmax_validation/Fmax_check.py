import numpy as np
from validation.common_utils.numeric_utils.statistics_calculation import rank_corr
from validation.common_utils.noise_metrics_utils.smooth_check import moving_avg
from validation.common_utils.noise_metrics_utils.noise_metric import noise_metric
from validation.common_utils.noise_metrics_utils.outlier_peak_detection import count_peaks

def validate_fmax_vs_x(x, y, ft_y=None, axis_name="Vg"):
    results = []
    score = 0

    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    mask = np.isfinite(x) & np.isfinite(y)

    if np.sum(mask) < 5:
        results.append(("Insufficient data", "Too few valid points for Fmax validation.", "orange"))
        return -1, results

    x = x[mask]
    y = y[mask]
    order = np.argsort(x)
    x = x[order]
    y = y[order]
    ys = moving_avg(y, 5)

    if np.any(y <= 0):
        results.append(("Sign check", "Fmax has non-physical values <= 0.", "red"))
        score -= 3
    else:
        results.append(("Sign check", "Fmax values are positive.", "green"))
        score += 1

    peaks = count_peaks(ys)
    if peaks <= 1:
        results.append(("Peak shape", "Fmax shows single broad dominant peak.", "green"))
        score += 1
    else:
        results.append(("Peak shape", f"Fmax shows multiple peaks ({peaks}).", "orange"))
        score -= 1

    noise = noise_metric(y)
    if noise < 0.08:
        results.append(("Smoothness", "Fmax curve is reasonably smooth.", "green"))
        score += 1
    else:
        results.append(("Smoothness", "Fmax curve is noisy; possible extraction issue.", "orange"))
        score -= 1

    if ft_y is not None:
        ft_y = np.asarray(ft_y, dtype=float)
        common_mask = np.isfinite(ft_y[mask][order])
        ft_use = ft_y[mask][order][common_mask]
        fmax_use = y[common_mask]

        if len(ft_use) >= 3:
            violating = int(np.sum(fmax_use > ft_use))
            if violating > 0:
                results.append(("Physical relation", f"Fmax exceeds Ft at {violating} point(s).", "red"))
                score -= 3
            else:
                results.append(("Physical relation", "Fmax remains below or equal to Ft.", "green"))
                score += 1

    if axis_name.lower() == "vd":
        corr = rank_corr(x, ys)
        if corr > 0.2:
            results.append(("VDS trend", "Fmax generally increases with VDS.", "green"))
            score += 1
        else:
            results.append(("VDS trend", "Fmax does not show expected increase with VDS.", "orange"))
            score -= 1

    return score, results

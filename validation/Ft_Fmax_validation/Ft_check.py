import numpy as np
from validation.common_utils.noise_metrics_utils.smooth_check import moving_avg
from validation.common_utils.noise_metrics_utils.noise_metric import noise_metric
from validation.common_utils.noise_metrics_utils.outlier_peak_detection import count_peaks

def validate_ft_vs_x(x, y, axis_name="Vg"):
    results = []
    score = 0

    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    mask = np.isfinite(x) & np.isfinite(y)

    if np.sum(mask) < 5:
        results.append(("Insufficient data", "Too few valid points for Ft validation.", "orange"))
        return -1, results

    x = x[mask]
    y = y[mask]
    order = np.argsort(x)
    x = x[order]
    y = y[order]
    ys = moving_avg(y, 5)

    if np.any(y <= 0):
        results.append(("Sign check", "Ft has non-physical values <= 0.", "red"))
        score -= 3
    else:
        results.append(("Sign check", "Ft values are positive.", "green"))
        score += 1

    peaks = count_peaks(ys)
    if peaks <= 1:
        results.append(("Peak shape", "Ft shows single smooth dominant peak.", "green"))
        score += 1
    else:
        results.append(("Peak shape", f"Ft shows multiple peaks ({peaks}).", "orange"))
        score -= 1

    noise = noise_metric(y)
    if noise < 0.06:
        results.append(("Smoothness", "Ft curve is smooth with no sharp discontinuity.", "green"))
        score += 1
    elif noise < 0.12:
        results.append(("Smoothness", "Ft curve has moderate ripple/noise.", "orange"))
    else:
        results.append(("Smoothness", "Ft curve is highly noisy/discontinuous.", "red"))
        score -= 2

    if axis_name.lower() == "vg":
        xspan = np.nanmax(x) - np.nanmin(x)
        if xspan > 0:
            peak_x = x[int(np.nanargmax(ys))]
            norm_peak = (peak_x - np.nanmin(x)) / xspan

            if norm_peak < 0.2:
                results.append(("Peak location", "Ft peak is too early in VGS sweep, likely subthreshold-side.", "orange"))
                score -= 1
            elif norm_peak < 0.85:
                results.append(("Peak location", "Ft peak location vs VGS looks physically reasonable.", "green"))
                score += 1
            else:
                results.append(("Peak location", "Ft peak is too late in VGS sweep.", "orange"))
                score -= 1

        dyn = (np.nanmax(ys) - np.nanmin(ys)) / max(np.nanmax(ys), 1e-18)
        if dyn < 0.10:
            results.append(("Trend shape", "Ft vs VGS is too flat; expected rise-peak-rolloff is weak.", "orange"))
            score -= 1
        else:
            results.append(("Trend shape", "Ft vs VGS shows expected rise and roll-off behavior.", "green"))
            score += 1

    elif axis_name.lower() == "vd":
        x_min, x_max = np.nanmin(x), np.nanmax(x)
        xspan = x_max - x_min
        if xspan > 0:
            left_mask = x <= (x_min + 0.5 * xspan)
            right_mask = x >= (x_min + 0.6 * xspan)

            left_slope = np.polyfit(x[left_mask], ys[left_mask], 1)[0] if np.sum(left_mask) >= 3 else 0.0
            right_slope = np.polyfit(x[right_mask], ys[right_mask], 1)[0] if np.sum(right_mask) >= 3 else 0.0

            if left_slope > 0:
                results.append(("Low-VDS trend", "Ft increases from low to moderate VDS.", "green"))
                score += 1
            else:
                results.append(("Low-VDS trend", "Ft does not increase properly in low/moderate VDS.", "orange"))
                score -= 1

            if abs(right_slope) <= 0.2 * max(abs(left_slope), 1e-12):
                results.append(("High-VDS trend", "Ft shows saturation / weak dependence at high VDS.", "green"))
                score += 1
            elif right_slope > 0:
                results.append(("High-VDS trend", "Ft keeps increasing strongly at high VDS; saturation is weak.", "orange"))
                score -= 1
            else:
                results.append(("High-VDS trend", "Ft decreases at high VDS.", "red"))
                score -= 2

    return score, results

import numpy as np


def validate_ft_fmax_ratio(ft, fmax):
    results = []
    score = 0

    ft = np.asarray(ft, dtype=float)
    fmax = np.asarray(fmax, dtype=float)

    mask = np.isfinite(ft) & np.isfinite(fmax) & (ft > 0)
    if np.sum(mask) < 3:
        results.append(("Ratio check", "Not enough valid Ft/Fmax points for ratio check.", "orange"))
        return -1, results

    ratio = fmax[mask] / ft[mask]
    median_ratio = float(np.median(ratio))

    if np.any(ratio > 1.0):
        results.append(("Ratio check", "Fmax/Ft > 1 detected. Non-physical extraction.", "red"))
        score -= 4
    else:
        results.append(("Ratio check", "No point has Fmax/Ft > 1.", "green"))
        score += 1

    if median_ratio < 0.1:
        results.append(("Ratio magnitude", f"Median Fmax/Ft={median_ratio:.3f} is too low. Possible high Rg/gds.", "orange"))
        score -= 2
    elif 0.3 <= median_ratio <= 0.9:
        results.append(("Ratio magnitude", f"Median Fmax/Ft={median_ratio:.3f} is in typical range.", "green"))
        score += 2
    else:
        results.append(("Ratio magnitude", f"Median Fmax/Ft={median_ratio:.3f} is outside typical range.", "orange"))
        score -= 1

    return score, results

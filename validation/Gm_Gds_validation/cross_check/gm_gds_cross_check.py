import numpy as np
from validation.common_utils.dataframe_operation.safe_numeric_check import safe_numeric_df
from validation.common_utils.dataframe_operation.df_generalize_name import pick_existing_column
from validation.common_utils.result_df.result_utils import add_result


def check_ft_consistency(keys, group, results, cfg):
    gm_col = cfg["gm_col"]
    ft_col = pick_existing_column(group, cfg["ft_candidates"])
    cgg_col = pick_existing_column(group, cfg["cgg_candidates"])

    if gm_col not in group.columns:
        return

    if ft_col is not None:
        temp = safe_numeric_df(group, [gm_col, ft_col]).dropna(subset=[gm_col, ft_col])
        if len(temp) >= 5:
            corr = temp[[gm_col, ft_col]].corr(method="spearman").iloc[0, 1]
            if np.isfinite(corr) and corr >= 0.4:
                add_result(results, "gm", keys, "gm and fT move consistently.", "green",
                           "fT Cross-Check", f"Spearman correlation ≈ {corr:.2f}.")
            elif np.isfinite(corr):
                add_result(results, "gm", keys, "gm and fT are poorly correlated.", "orange",
                           "fT Cross-Check", f"Spearman correlation ≈ {corr:.2f}.")

    if cgg_col is not None and ft_col is not None:
        temp = safe_numeric_df(group, [gm_col, cgg_col, ft_col]).dropna(subset=[gm_col, cgg_col, ft_col])
        if len(temp) >= 5:
            cgg = temp[cgg_col].to_numpy(dtype=float)
            gm = temp[gm_col].to_numpy(dtype=float)
            ft_meas = temp[ft_col].to_numpy(dtype=float)

            mask = np.isfinite(cgg) & np.isfinite(gm) & np.isfinite(ft_meas) & (np.abs(cgg) > cfg["eps"])
            if np.any(mask):
                ft_est = gm[mask] / (2.0 * np.pi * np.abs(cgg[mask]))
                rel_err = np.nanmedian(
                    np.abs(ft_est - ft_meas[mask]) / np.maximum(np.abs(ft_meas[mask]), cfg["eps"])
                )

                if rel_err <= 0.5:
                    add_result(results, "gm", keys, "gm is consistent with fT and Cgg.", "green",
                               "fT Cross-Check", f"Median relative mismatch ≈ {100 * rel_err:.1f}%.")
                else:
                    add_result(results, "gm", keys, "gm is not consistent with fT and Cgg.", "orange",
                               "fT Cross-Check", f"Median relative mismatch ≈ {100 * rel_err:.1f}%.")

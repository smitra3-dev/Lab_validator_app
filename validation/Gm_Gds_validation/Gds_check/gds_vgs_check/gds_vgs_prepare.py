# gds_vgs_prepare.py

from validation.common_utils.dataframe_operation.safe_numeric_check import safe_numeric_df


def prepare_gds_vgs_dataframe(group, cfg):
    cols = [cfg["gds_col"], cfg["vg_col"], cfg["vd_col"], cfg["gm_col"]]
    temp = safe_numeric_df(group, cols).dropna(subset=[cfg["gds_col"], cfg["vg_col"], cfg["vd_col"]])

    if len(temp) < cfg["min_points_axis"]:
        return None

    return temp

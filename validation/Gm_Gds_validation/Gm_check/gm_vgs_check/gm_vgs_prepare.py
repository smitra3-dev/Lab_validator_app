#gm_vgs_prepare
from validation.common_utils.dataframe_operation.safe_numeric_check import safe_numeric_df


def prepare_gm_vgs_dataframe(group, cfg):
    cols = [cfg["gm_col"], cfg["vg_col"], cfg["vd_col"], cfg["id_col"]]

    temp = safe_numeric_df(group, cols)
    temp = temp.dropna(subset=[cfg["gm_col"], cfg["vg_col"], cfg["vd_col"]])

    if len(temp) < cfg["min_points_axis"]:
        return None

    return temp

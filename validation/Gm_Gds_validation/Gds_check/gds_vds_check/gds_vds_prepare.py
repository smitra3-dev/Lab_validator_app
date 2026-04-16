#gds_vds_prepare.py
from validation.common_utils.dataframe_operation.safe_numeric_check  import safe_numeric_df


def prepare_gds_vds_dataframe(group, cfg):
    cols = [cfg["gds_col"], cfg["vg_col"], cfg["vd_col"]]
    temp = safe_numeric_df(group, cols).dropna(subset=cols)

    if len(temp) < cfg["min_points_axis"]:
        return None

    return temp

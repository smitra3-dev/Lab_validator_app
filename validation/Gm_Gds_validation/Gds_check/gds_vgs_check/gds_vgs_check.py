#gds_vgs_check.py

from .gds_vgs_prepare import prepare_gds_vgs_dataframe
from .gds_vgs_monotonicity_check import check_gds_vgs_monotonicity
from .gds_intrinsic_gain_check import check_intrinsic_gain


def check_gds_vs_vgs(keys, group, results, cfg):
    gds_col = cfg["gds_col"]
    vg_col = cfg["vg_col"]
    vd_col = cfg["vd_col"]
    gm_col = cfg["gm_col"]

    if gds_col not in group.columns or vg_col not in group.columns or vd_col not in group.columns:
        return

    temp = prepare_gds_vgs_dataframe(group, cfg)
    if temp is None:
        return

    for vd_val, vd_group in temp.groupby(vd_col):
        if len(vd_group) < cfg["min_points_axis"]:
            continue

        vd_group = vd_group.sort_values(vg_col)

        x = vd_group[vg_col].to_numpy(dtype=float)
        y = vd_group[gds_col].to_numpy(dtype=float)

        check_gds_vgs_monotonicity(keys, vd_val, x, y, results, cfg)

        if gm_col in vd_group.columns:
            gm = vd_group[gm_col].to_numpy(dtype=float)
            check_intrinsic_gain(keys, vd_val, gm, y, results, cfg)

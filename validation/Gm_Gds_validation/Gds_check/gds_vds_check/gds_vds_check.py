from .gds_vds_prepare import prepare_gds_vds_dataframe
from .gds_vds_metrics import compute_gds_drop_ratio
from .gds_vds_monotonicity_check import check_gds_vds_monotonicity
from .gds_vds_drop_ratio_check import check_gds_vds_drop_ratio


def check_gds_vs_vds(keys, group, results, cfg):
    gds_col = cfg["gds_col"]
    vg_col = cfg["vg_col"]
    vd_col = cfg["vd_col"]

    if gds_col not in group.columns or vg_col not in group.columns or vd_col not in group.columns:
        return

    temp = prepare_gds_vds_dataframe(group, cfg)
    if temp is None:
        return

    for vg_val, vg_group in temp.groupby(vg_col):
        if len(vg_group) < cfg["min_points_axis"]:
            continue

        vg_group = vg_group.sort_values(vd_col)

        vd_values = vg_group[vd_col].to_numpy(dtype=float)
        y = vg_group[gds_col].to_numpy(dtype=float)

        check_gds_vds_monotonicity(keys, vg_val, vd_values, y, results, cfg)

        drop_ratio = compute_gds_drop_ratio(y, cfg["eps"])
        check_gds_vds_drop_ratio(keys, vg_val, drop_ratio, results, cfg)

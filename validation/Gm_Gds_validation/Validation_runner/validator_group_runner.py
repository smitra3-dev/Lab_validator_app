#validator_group_runner
from validation.Gm_Gds_validation.Gm_check.gm_runner import run_all_gm_checks
from validation.Gm_Gds_validation.Gds_check.gds_runner import run_all_gds_checks
from validation.Gm_Gds_validation.cross_check.gm_gds_cross_check import check_ft_consistency


def run_group_validations(keys, group, results, cfg, run_gm, run_gds):
    """
    Run gm/gds validation checks for one grouped dataframe.
    """
    if group is None or len(group) == 0:
        return

    group = group.copy()

    if run_gm and cfg["gm_col"] in group.columns:
        run_all_gm_checks(keys, group, results, cfg)
        check_ft_consistency(keys, group, results, cfg)

    if run_gds and cfg["gds_col"] in group.columns:
        run_all_gds_checks(keys, group, results, cfg)

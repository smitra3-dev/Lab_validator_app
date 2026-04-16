#gm_runner
from .gm_sign_check import check_gm_sign_magnitude
from .gm_frequency_check import check_gm_freq_behavior
from validation.Gm_Gds_validation.Gm_check.gm_vgs_check.gm_vgs_check import check_gm_vs_vgs
from validation.Gm_Gds_validation.Gm_check.gm_vds_check.gm_vds_check import check_gm_vs_vds


def run_all_gm_checks(keys, group, results, cfg):
    """
    Run all gm-related validation checks.
    """
    check_gm_sign_magnitude(keys, group, results, cfg)
    check_gm_freq_behavior(keys, group, results, cfg)
    check_gm_vs_vgs(keys, group, results, cfg)
    check_gm_vs_vds(keys, group, results, cfg)

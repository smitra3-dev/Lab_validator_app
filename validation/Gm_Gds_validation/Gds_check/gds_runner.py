#gds_runner
from .gds_sign_check import check_gds_sign_magnitude
from validation.Gm_Gds_validation.Gds_check.gds_frequency_check.gds_frequency_check import check_gds_freq_behavior
from validation.Gm_Gds_validation.Gds_check.gds_vds_check.gds_vds_check import check_gds_vs_vds
from validation.Gm_Gds_validation.Gds_check.gds_vgs_check.gds_vgs_check import check_gds_vs_vgs


def run_all_gds_checks(keys, group, results, cfg):
    """
    Run all gds-related validation checks.
    """
    check_gds_sign_magnitude(keys, group, results, cfg)
    check_gds_freq_behavior(keys, group, results, cfg)
    check_gds_vs_vds(keys, group, results, cfg)
    check_gds_vs_vgs(keys, group, results, cfg)

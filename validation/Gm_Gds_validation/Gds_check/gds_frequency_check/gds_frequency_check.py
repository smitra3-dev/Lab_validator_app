#gds_frequency_check.py
from validation.Gm_Gds_validation.gm_gds_helper.frequency_splitter import split_lf_hf
from .gds_frequency_subset import build_gds_frequency_subset
from .gds_lf_frequency_check import check_gds_lf_behavior
from .gds_hf_frequency_check import check_gds_hf_behavior


def check_gds_freq_behavior(keys, group, results, cfg):
    subset = build_gds_frequency_subset(group, cfg)
    if subset is None:
        return

    lf, hf, fnqs = split_lf_hf(subset, cfg)

    check_gds_lf_behavior(keys, lf, results, cfg)
    check_gds_hf_behavior(keys, hf, results, cfg, fnqs)


from validation.Gm_Gds_validation.gm_gds_helper.frequency_splitter import split_lf_hf
from .gm_frequency_subset import build_gm_frequency_subset
from .gm_lf_frequency_check import check_gm_lf_behavior
from .gm_hf_frequency_check import check_gm_hf_behavior

def check_gm_freq_behavior(keys, group, results, cfg):
    subset = build_gm_frequency_subset(group, cfg)
    if subset is None:
        return

    lf, hf, fnqs = split_lf_hf(subset, cfg)

    check_gm_lf_behavior(keys, lf, results, cfg)
    check_gm_hf_behavior(keys, hf, results, cfg, fnqs)

#capacitance_config.py
CAPACITANCE_CONFIG = {
    "supported_caps": ["Cgs", "Cgd", "Cgg"],
    "min_points": 2,
    "small_eps": 1e-18,

    # Frequency checks
    "freq_rel_span_warn": 1.0,
    "freq_osc_warn": 0.45,

    # Vg checks
    "cgs_vg_mono_good": 0.55,
    "cgg_vg_flat_warn": 0.05,
    "cgd_vg_rise_warn": 0.75,

    # Vd checks
    "cgd_vd_mono_good": 0.55,
    "vd_rel_span_warn": 0.40,

    # Id checks
    "id_rel_span_flat_warn": 0.03,
    "id_osc_warn": 0.45,

    # Cross checks
    "cgg_sum_fail_fraction": 0.30,
    "cgg_sum_fail_scale": 0.80,
    "cgg_sum_warn_rel_err": 0.40,
    "cgs_cgd_fail_ratio": 1.0,
    "cgs_cgd_warn_ratio": 2.0,
}

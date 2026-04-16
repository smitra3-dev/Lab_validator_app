#__init__ gds
# --- Core validation entry points (used by runner) ---
from .gds_sign_check import check_gds_sign_magnitude
from .gds_frequency_check.gds_frequency_check import check_gds_freq_behavior
from .gds_vds_check.gds_vds_check import check_gds_vs_vds
from .gds_vgs_check.gds_vgs_check import check_gds_vs_vgs

# --- Runner ---
from .gds_runner import run_all_gds_checks


# --- Optional: expose internal helpers (useful for debugging / testing) ---
from validation.Gm_Gds_validation.Gm_Gds_ratio.gm_gds_ratio_check import compute_gm_gds_ratio

from validation.Gm_Gds_validation.Gds_check.gds_frequency_check.gds_frequency_subset import build_gds_frequency_subset
from validation.Gm_Gds_validation.Gds_check.gds_frequency_check.gds_lf_frequency_check import check_gds_lf_behavior
from validation.Gm_Gds_validation.Gds_check.gds_frequency_check.gds_hf_frequency_check import check_gds_hf_behavior

from validation.Gm_Gds_validation.Gds_check.gds_vds_check.gds_vds_prepare import prepare_gds_vds_dataframe
from validation.Gm_Gds_validation.Gds_check.gds_vds_check.gds_vds_metrics import compute_gds_drop_ratio
from validation.Gm_Gds_validation.Gds_check.gds_vds_check.gds_vds_monotonicity_check import check_gds_vds_monotonicity
from validation.Gm_Gds_validation.Gds_check.gds_vds_check.gds_vds_drop_ratio_check import check_gds_vds_drop_ratio

from validation.Gm_Gds_validation.Gds_check.gds_vgs_check.gds_vgs_prepare import prepare_gds_vgs_dataframe
from validation.Gm_Gds_validation.Gds_check.gds_vgs_check.gds_vgs_monotonicity_check import check_gds_vgs_monotonicity
from validation.Gm_Gds_validation.Gds_check.gds_vgs_check.gds_intrinsic_gain_check import check_intrinsic_gain


__all__ = [
    # --- Main callable checks ---
    "check_gds_sign_magnitude",
    "check_gds_freq_behavior",
    "check_gds_vs_vds",
    "check_gds_vs_vgs",

    # --- Runner ---
    "run_all_gds_checks",

    # --- Optional helpers (debug / reuse) ---
    "compute_gm_gds_ratio",
    "build_gds_frequency_subset",
    "check_gds_lf_behavior",
    "check_gds_hf_behavior",
    "prepare_gds_vds_dataframe",
    "compute_gds_drop_ratio",
    "check_gds_vds_monotonicity",
    "check_gds_vds_drop_ratio",
    "prepare_gds_vgs_dataframe",
    "check_gds_vgs_monotonicity",
    "check_intrinsic_gain",
]

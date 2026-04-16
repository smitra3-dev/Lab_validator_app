from rf_core.rf_calculation.rf_h21_calculator import calculate_h21_metrics
from rf_core.rf_calculation.rf_K_factor_calculator import calculate_stability_factor
from rf_core.rf_calculation.rf_msgmag_calculator import calculate_power_gain_metrics
from rf_core.rf_calculation.rf_ft_fmax_calculator import calculate_ft_fmax_metrics
from rf_core.rf_calculation.rf_gm_gds_calculator import calculate_transconductance_metrics
from rf_core.rf_calculation.rf_capacitance_calculator import calculate_capacitance_metrics

#updated 13/06/26 subfolder access

def calculate_all_rf_metrics(work):
    work = calculate_h21_metrics(work)
    work = calculate_stability_factor(work)
    work = calculate_power_gain_metrics(work)
    work = calculate_ft_fmax_metrics(work)
    work = calculate_transconductance_metrics(work)
    work = calculate_capacitance_metrics(work)
    return work

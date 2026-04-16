import numpy as np
from validation.common_utils.dataframe_operation.df_copy import to_pandas
from validation.common_utils.dataframe_operation.df_generalize_name import pick_existing_column


from validation.common_utils.noise_metrics_utils.smooth_check import moving_avg
from validation.common_utils.noise_metrics_utils.noise_metric import noise_metric
from validation.common_utils.noise_metrics_utils.outlier_peak_detection import count_peaks

from validation.common_utils.numeric_utils.statistics_calculation import rank_corr
from validation.common_utils.numeric_utils.conversion_num_series import safe_num

def prepare_curve_data(group, x_axis, ft_names, fmax_names):
    gpdf = to_pandas(group)
    if gpdf.empty:
        return None

    x_col = pick_existing_column(gpdf, [x_axis])
    ft_col = pick_existing_column(gpdf, ft_names)
    fmax_col = pick_existing_column(gpdf, fmax_names)

    return {
        "df": gpdf,
        "x_col": x_col,
        "ft_col": ft_col,
        "fmax_col": fmax_col,
    }

#rf_anomaly_detector

import numpy as np
import pandas as pd

from validation.Anomaly_predictor.Trend_analysis.trend_detector import detect_trend
from validation.Anomaly_predictor.Trend_analysis.trend_predictor import predict_trend
from .anomaly_input_prep import prepare_anomaly_dataframe
from .anomaly_window_utils import get_window_blocks, has_minimum_points
from .anomaly_residuals import compute_residual_error
from .anomaly_slopes import compute_slope_error
from .anomaly_scoring import combine_anomaly_errors
from .anomaly_labeling import label_block_scores
from .anomaly_debug import build_initial_trend_message, build_block_debug_message


def _build_block_results(x_col, y_col, x_block, y_block, scores, labels):
    rows = []

    for j in range(len(y_block)):
        rows.append({
            x_col: x_block[j],
            y_col: y_block[j],
            "error": scores[j],
            "label": labels[j],
        })

    return rows


def detect_rf_anomalies(df, x_col, y_col, window=5, red_thresh=0.6, yellow_thresh=0.3):
    """
    Detect local anomalies in RF curves using trend residuals and slope changes.
    """
    prepared = prepare_anomaly_dataframe(df, x_col, y_col)
    if prepared is None or len(prepared) < 3:
        return pd.DataFrame(columns=[x_col, y_col, "error", "label"]), []

    x = prepared[x_col].to_numpy(dtype=float)
    y = prepared[y_col].to_numpy(dtype=float)

    results = []
    debug_log = []

    init_window = min(window, len(prepared))
    trend_type, coef = detect_trend(x[:init_window], y[:init_window])
    debug_log.append(build_initial_trend_message(x_col, y_col, trend_type))

    i = 0
    while i < len(prepared):
        x_block, y_block = get_window_blocks(x, y, i, window)

        if not has_minimum_points(x_block, min_points=3):
            break

        y_pred = predict_trend(x_block, trend_type, coef)
        residual_error = compute_residual_error(y_block, y_pred)
        slope_error = compute_slope_error(x_block, y_block)

        combined_error = combine_anomaly_errors(slope_error, residual_error)
        block_labels = label_block_scores(
            combined_error,
            red_thresh=red_thresh,
            yellow_thresh=yellow_thresh,
        )

        results.extend(
            _build_block_results(
                x_col=x_col,
                y_col=y_col,
                x_block=x_block,
                y_block=y_block,
                scores=combined_error,
                labels=block_labels,
            )
        )

        debug_log.append(build_block_debug_message(x_col, x_block, block_labels))
        i += window

    result_df = pd.DataFrame(results)
    return result_df, debug_log

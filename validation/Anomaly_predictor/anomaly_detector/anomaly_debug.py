#anomaly_debug

def build_initial_trend_message(x_col, y_col, trend_type):
    return f"[INIT] {y_col} vs {x_col} → Trend: {trend_type}"


def build_block_debug_message(x_col, x_block, block_labels):
    """
    Build debug message for one processed block.
    """
    if block_labels.count("red") >= 2:
        return f"[NOISE] {x_col}: {round(x_block[0], 3)} → {round(x_block[-1], 3)}"

    if block_labels.count("red") == 1:
        idx = block_labels.index("red")
        return f"[SPIKE] {x_col}={round(x_block[idx], 3)}"

    return f"[PASS] {x_col}: {round(x_block[0], 3)} → {round(x_block[-1], 3)}"

#anomaly_window_utils
def get_window_blocks(x, y, start_idx, window):
    """
    Return one x/y block for sliding fixed-window processing.
    """
    x_block = x[start_idx:start_idx + window]
    y_block = y[start_idx:start_idx + window]
    return x_block, y_block


def has_minimum_points(x_block, min_points=3):
    """
    Check whether current window has sufficient data.
    """
    return len(x_block) >= min_points

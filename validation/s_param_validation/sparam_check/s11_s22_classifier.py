
def classify_s11_s22(
    avg_val: float,
    good_match_db: float = -10,
    acceptable_match_db: float = -5,
) -> tuple[str, str]:
    """
    Classify return loss quality for S11 or S22.

    Parameters
    ----------
    avg_val : float
        Average S11 or S22 value in dB.
    good_match_db : float
        Threshold for good match.
    acceptable_match_db : float
        Threshold for acceptable match.

    Returns
    -------
    tuple[str, str]
        (message, color)
    """
    if avg_val < 0:
        if avg_val < good_match_db:
            return "Good Match", "green"
        if avg_val < acceptable_match_db:
            return "Acceptable Match", "orange"
        return "Measurement is okay", "lightgreen"

    return "Check the measurement!!", "red"

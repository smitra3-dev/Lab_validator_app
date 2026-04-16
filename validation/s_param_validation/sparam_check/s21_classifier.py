#s21classifier

"""
S21 classification rules.
"""


def classify_s21(avg_val: float) -> tuple[str, str]:
    """
    Classify device type based on average S21 in dB.

    Parameters
    ----------
    avg_val : float
        Average S21 value in dB.

    Returns
    -------
    tuple[str, str]
        (message, color)
    """
    if avg_val > 0:
        return "Active device", "purple"
    return "Passive device", "lightblue"

#s12 classifier 

def classify_s12(
    avg_val: float,
    good_isolation_db: float = -20,
) -> tuple[str, str]:
    """
    Classify reverse isolation quality from S12.

    Parameters
    ----------
    avg_val : float
        Average S12 value in dB.
    good_isolation_db : float
        Threshold for good isolation.

    Returns
    -------
    tuple[str, str]
        (message, color)
    """
    if avg_val < good_isolation_db:
        return "Good Isolation", "green"
    return "Check measurement!!", "red"

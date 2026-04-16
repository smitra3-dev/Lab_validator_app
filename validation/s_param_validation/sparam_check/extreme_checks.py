#extreme_checks.py
"""
Extreme value screening for S-parameter dB data.
"""

from typing import Iterable, Optional, Tuple


def check_extreme(
    values: Iterable[float],
    high_db: float = 30,
    low_db: float = -80,
) -> Optional[Tuple[str, str]]:
    """
    Check whether any value exceeds allowed dB limits.

    Parameters
    ----------
    values : Iterable[float]
        Sequence of S-parameter values in dB.
    high_db : float
        Upper acceptable limit.
    low_db : float
        Lower acceptable limit.

    Returns
    -------
    Optional[Tuple[str, str]]
        (message, color) if violation found, otherwise None.
    """
    for value in values:
        if value > high_db or value < low_db:
            return f"Please check the measurement (value={round(value, 2)} dB)", "red"
    return None

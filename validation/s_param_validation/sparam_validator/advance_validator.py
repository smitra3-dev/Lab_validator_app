#advance validator 

from .config_loader import load_sparam_config
from .single_sparam_validator import (
    is_supported_sparam,
    validate_single_sparam_group,
)
from .reciprocity_validator import (
    should_run_reciprocity,
    validate_reciprocity_group,
)


def validate_sparams_advanced(groups, params, config=None):
    """
    Run advanced S-parameter validation on grouped data.

    Parameters
    ----------
    groups : iterable
        Iterable of (keys, group) pairs.
    params : list[str]
        Parameter names selected for validation.
    config : dict | None
        Optional config overrides.

    Returns
    -------
    list[dict]
        Validation result dictionaries.
    """
    cfg = load_sparam_config(config)
    results = []

    group_list = list(groups)

    for param in params:
        if not is_supported_sparam(param):
            continue

        for keys, group in group_list:
            result = validate_single_sparam_group(param, keys, group, cfg)
            if result is not None:
                results.append(result)

    if should_run_reciprocity(params):
        for keys, group in group_list:
            result = validate_reciprocity_group(keys, group, cfg)
            if result is not None:
                results.append(result)

    return results

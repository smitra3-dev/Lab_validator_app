#gm_gds_validator
from .validator_config import build_gm_gds_config
from .validator_flags import resolve_validation_flags
from .validator_result_builder import initialize_validation_results
from .validator_group_runner import run_group_validations


def validate_gm_gds(groups, selected_param, config=None):
    """
    Main gm/gds validator entrypoint.
    """
    cfg = build_gm_gds_config(config)
    run_gm, run_gds = resolve_validation_flags(selected_param)
    results = initialize_validation_results()

    for keys, group in groups:
        run_group_validations(
            keys=keys,
            group=group,
            results=results,
            cfg=cfg,
            run_gm=run_gm,
            run_gds=run_gds,
        )

    return results

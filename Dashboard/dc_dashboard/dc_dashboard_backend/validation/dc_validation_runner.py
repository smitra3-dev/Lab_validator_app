##dashboard/dc/validation/dc_validation_runner.py

from .dc_validation_sections import (
    build_dc_gm_gds_children,
    build_dc_cap_children,
    build_dc_ftfmax_children,
)


def run_dc_validation_sections(pdf, valid_params):
    return (
        build_dc_gm_gds_children(pdf, valid_params),
        build_dc_cap_children(pdf, valid_params),
        build_dc_ftfmax_children(pdf, valid_params),
    )

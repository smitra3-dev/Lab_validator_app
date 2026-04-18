
#dashboard/gain/validation/gain_validation_runner.py
from .gain_validation_sections import (
    build_gain_gm_gds_children,
    build_gain_ftfmax_children,
)


def run_gain_validation_sections(pdf, valid_params):
    return (
        build_gain_gm_gds_children(pdf, valid_params),
        build_gain_ftfmax_children(pdf, valid_params),
    )

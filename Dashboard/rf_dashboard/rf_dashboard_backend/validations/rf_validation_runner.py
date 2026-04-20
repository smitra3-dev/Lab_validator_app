from .rf_validation_sections import (
    build_generic_validation_children,
    build_sparam_validation_children,
    build_h21_validation_children,
    build_cap_validation_children,
    build_ftfmax_validation_children,
)


def run_rf_validation_sections(pdf, valid_params, xscale, yscale):
    return (
        build_generic_validation_children(pdf, valid_params, xscale),
        build_sparam_validation_children(pdf, valid_params),
        build_h21_validation_children(pdf, valid_params, xscale, yscale),
        build_cap_validation_children(pdf, valid_params),
        build_ftfmax_validation_children(pdf, valid_params),
    )
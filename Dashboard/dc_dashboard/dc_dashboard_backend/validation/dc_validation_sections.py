##dashboard/dc/validation/dc_validation_sections.py

from dash import html

from validation.capacitance_validation.capacitance_validator import validate_capacitances
from validation.Ft_Fmax_validation.Ft_Fmax_validator import validate_ft_fmax
from validation.Gm_Gds_validation.Validation_runner.gm_gds_validator import validate_gm_gds

from ..config.dc_constants import (
    DC_GROUP_COLS,
    DC_CAP_PARAMS,
    DC_FTFMAX_PARAMS,
)
from .dc_validation_cards import build_dc_validation_card


def build_dc_gm_gds_children(pdf, valid_params):
    selected = [p for p in valid_params if p in {"gm", "gds"}]
    if not selected:
        return ["No gm/gds validation triggered"]

    groups = list(pdf.groupby(DC_GROUP_COLS))
    children = []

    for selected_param in selected:
        results = validate_gm_gds(groups, selected_param=selected_param)

        for res in results:
            lines = [
                html.Div(
                    f"Result : {res.get('message', 'NA')}",
                    style={"marginTop": "6px", "fontWeight": "bold", "color": res.get("color", "black")},
                ),
                html.Div(
                    f"Detail : {res.get('detail', '')}",
                    style={"marginTop": "4px", "fontStyle": "italic"},
                ),
            ]
            children.append(
                build_dc_validation_card(
                    param=res.get("param", selected_param),
                    keys=res.get("keys", ("NA",) * 5),
                    lines=lines,
                    color=res.get("color", "black"),
                )
            )

    return children or ["No gm/gds validation triggered"]


def build_dc_cap_children(pdf, valid_params):
    if not any(p in DC_CAP_PARAMS for p in valid_params):
        return ["No capacitance validation triggered"]

    groups = list(pdf.groupby(DC_GROUP_COLS))
    results = validate_capacitances(iter(groups), "Vg", valid_params)

    children = []
    for res in results:
        lines = [
            html.Div(f"Status : {res.get('status', 'NA')} (noise={res.get('noise', 'NA')})", style={"marginTop": "6px"}),
            html.Div(f"Comment : {res.get('comment', '')}", style={"marginTop": "4px", "fontStyle": "italic"}),
        ]
        children.append(
            build_dc_validation_card(
                param=res.get("param", "NA"),
                keys=res.get("keys", ("NA",) * 5),
                lines=lines,
                color=res.get("color", "black"),
            )
        )

    return children or ["No capacitance validation triggered"]


def build_dc_ftfmax_children(pdf, valid_params):
    selected = [p for p in valid_params if p in DC_FTFMAX_PARAMS]
    if not selected:
        return ["No Ft/Fmax validation triggered"]

    groups = list(pdf.groupby(DC_GROUP_COLS))
    children = []

    for selected_param in selected:
        results = validate_ft_fmax(groups, selected_param=selected_param, x_axis="Vg")

        for res in results:
            lines = [
                html.Div(f"Section : {res.get('section', '')}", style={"marginTop": "6px", "fontWeight": "bold", "color": res.get("color", "black")}),
                html.Div(f"Result : {res.get('message', '')}", style={"marginTop": "4px"}),
                html.Div(f"Detail : {res.get('detail', '')}", style={"marginTop": "4px", "fontStyle": "italic"}),
            ]
            children.append(
                build_dc_validation_card(
                    param=res.get("param", selected_param),
                    keys=res.get("keys", ("NA",) * 5),
                    lines=lines,
                    color=res.get("color", "black"),
                )
            )

    return children or ["No Ft/Fmax validation triggered"]

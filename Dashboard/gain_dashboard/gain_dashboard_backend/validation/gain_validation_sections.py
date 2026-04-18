#dashboard/gain/validation/gain_validation_sections.py
from dash import html

from validation.Ft_Fmax_validation.Ft_Fmax_validator import validate_ft_fmax
from validation.Gm_Gds_validation.Validation_runner.gm_gds_validator import validate_gm_gds

from ..config.gain_constants import (
    GAIN_GROUP_COLS,
    GAIN_FTFMAX_PARAMS,
)
from .gain_validation_cards import build_gain_validation_card


def build_gain_gm_gds_children(pdf, valid_params):
    selected = [p for p in valid_params if p in {"gm", "gds"}]
    if not selected:
        return ["No gm/gds validation triggered"]

    groups = list(pdf.groupby(GAIN_GROUP_COLS))
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
                build_gain_validation_card(
                    param=res.get("param", selected_param),
                    keys=res.get("keys", ("NA",) * 5),
                    lines=lines,
                    color=res.get("color", "black"),
                )
            )

    return children or ["No gm/gds validation triggered"]


def build_gain_ftfmax_children(pdf, valid_params):
    selected = [p for p in valid_params if p in GAIN_FTFMAX_PARAMS]
    if not selected:
        return ["No Ft/Fmax validation triggered"]

    groups = list(pdf.groupby(GAIN_GROUP_COLS))
    children = []

    for selected_param in selected:
        results = validate_ft_fmax(groups, selected_param=selected_param, x_axis="Id")

        for res in results:
            lines = [
                html.Div(f"Section : {res.get('section', '')}", style={"marginTop": "6px", "fontWeight": "bold", "color": res.get("color", "black")}),
                html.Div(f"Result : {res.get('message', '')}", style={"marginTop": "4px"}),
                html.Div(f"Detail : {res.get('detail', '')}", style={"marginTop": "4px", "fontStyle": "italic"}),
            ]
            children.append(
                build_gain_validation_card(
                    param=res.get("param", selected_param),
                    keys=res.get("keys", ("NA",) * 5),
                    lines=lines,
                    color=res.get("color", "black"),
                )
            )

    return children or ["No Ft/Fmax validation triggered"]

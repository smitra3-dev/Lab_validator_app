##validation/rf_validation_sections.py
from dash import html


#from ValidationBlock import validate_data_detailed
from validation.s_param_validation.sparam_validator.advance_validator import validate_sparams_advanced
from validation.h21_validation.h21_validator import validate_h21
from validation.capacitance_validation.capacitance_validator import validate_capacitances
from validation.Ft_Fmax_validation.Ft_Fmax_validator import validate_ft_fmax
from validation.Gm_Gds_validation.Validation_runner.gm_gds_validator import validate_gm_gds

#need to investigate


from ..config.rf_constants import (
    RF_GROUP_COLS,
    RF_CAP_PARAMS,
    RF_FTFMAX_PARAMS,
    RF_GENERIC_EXCLUDE_PARAMS,
)
from .rf_validation_cards import build_validation_card


def build_generic_validation_children(pdf, valid_params, xscale):
    validation_children = []
    validation_pdf = pdf.copy()

    if xscale == "log":
        validation_pdf = validation_pdf[validation_pdf["Fs"] > 0]

    if not validation_pdf.empty:
        groups = validation_pdf.groupby(RF_GROUP_COLS)
        generic_params = [p for p in valid_params if p not in RF_GENERIC_EXCLUDE_PARAMS]
        results = validate_data_detailed(groups, generic_params) if generic_params else []

        for res in results:
            lines = [
                html.Div(f"Status : {res.get('status', 'NA')} (noise={res.get('noise', 'NA')})", style={"marginTop": "6px"}),
                html.Div(f"Comment : {res.get('comment', '')}", style={"marginTop": "4px", "fontStyle": "italic"}),
            ]
            validation_children.append(
                build_validation_card(
                    param=res.get("param", "NA"),
                    keys=res.get("keys", ("NA",) * 6),
                    lines=lines,
                    color=res.get("color", "black"),
                )
            )

    return validation_children or ["No validation results"]


def build_sparam_validation_children(pdf, valid_params):
    groups = pdf.groupby(RF_GROUP_COLS)
    results = validate_sparams_advanced(groups, valid_params)

    children = []
    for res in results:
        lines = [
            html.Div(
                f"Result : {res['message']}",
                style={"marginTop": "6px", "fontWeight": "bold", "color": res["color"]},
            )
        ]
        children.append(
            build_validation_card(
                param=res["param"],
                keys=res["keys"],
                lines=lines,
                color=res["color"],
            )
        )

    return children or ["No S-parameter validation triggered"]


def build_h21_validation_children(pdf, valid_params, xscale, yscale):
    children = []

    if "h21_dB" not in valid_params or "h21_dB" not in pdf.columns:
        return ["No h21 validation triggered"]

    for keys, group in pdf.groupby(RF_GROUP_COLS):
        group = group.sort_values("Fs").copy()

        if xscale == "log":
            group = group[group["Fs"] > 0]
        if yscale == "log":
            group = group[group["h21_dB"] > 0]

        if group.empty or len(group) < 2:
            continue

        message, color = validate_h21(group["Fs"].values, group["h21_dB"].values)
        lines = [
            html.Div(
                f"Result: {message}",
                style={"marginTop": "4px", "fontWeight": "bold", "fontStyle": "italic", "color": color},
            )
        ]
        children.append(build_validation_card("h21", keys, lines, color))

    return children or ["No h21 validation triggered"]


def build_cap_validation_children(pdf, valid_params):
    if not any(p in RF_CAP_PARAMS for p in valid_params):
        return ["No capacitance validation triggered"]

    groups = pdf.groupby(RF_GROUP_COLS)
    cap_results = validate_capacitances(groups, "Fs", valid_params)

    children = []
    for res in cap_results:
        lines = [
            html.Div(f"Status : {res['status']} (noise={res['noise']})", style={"marginTop": "6px"}),
            html.Div(f"Comment : {res['comment']}", style={"marginTop": "4px", "fontStyle": "italic"}),
        ]
        children.append(
            build_validation_card(
                param=res["param"],
                keys=res["keys"],
                lines=lines,
                color=res["color"],
            )
        )

    return children or ["No capacitance validation triggered"]


def build_ftfmax_validation_children(pdf, valid_params):
    children = []
    special_params = [p for p in valid_params if p in RF_FTFMAX_PARAMS]

    if not special_params:
        return ["No Ft/Fmax validation triggered"]

    groups = list(pdf.groupby(RF_GROUP_COLS))

    for param in special_params:
        results = validate_ft_fmax(groups, selected_param=param, x_axis="Fs")
        for res in results:
            lines = [
                html.Div(f"Section : {res['section']}", style={"marginTop": "6px", "fontWeight": "bold", "color": res["color"]}),
                html.Div(f"Result : {res['message']}", style={"marginTop": "4px"}),
                html.Div(f"Detail : {res['detail']}", style={"marginTop": "4px", "fontStyle": "italic"}),
            ]
            children.append(
                build_validation_card(
                    param=res["param"],
                    keys=res["keys"],
                    lines=lines,
                    color=res["color"],
                )
            )

    return children or ["No Ft/Fmax validation triggered"]


def build_gm_gds_validation_children(pdf, valid_params):
    if not any(p in {"gm", "gds"} for p in valid_params):
        return ["No gm/gds validation triggered"]

    groups = list(pdf.groupby(RF_GROUP_COLS))
    children = []

    for selected_param in [p for p in valid_params if p in {"gm", "gds"}]:
        results = validate_gm_gds(groups, selected_param=selected_param)

        for res in results:
            lines = [
                html.Div(
                    f"Result : {res.get('message', res.get('status', 'NA'))}",
                    style={"marginTop": "6px"}
                ),
                html.Div(
                    f"Detail : {res.get('detail', res.get('comment', ''))}",
                    style={"marginTop": "4px", "fontStyle": "italic"}
                ),
            ]
            children.append(
                build_validation_card(
                    param=res.get("param", selected_param),
                    keys=res.get("keys", ("NA",) * 6),
                    lines=lines,
                    color=res.get("color", "black"),
                )
            )

    return children or ["No gm/gds validation triggered"]
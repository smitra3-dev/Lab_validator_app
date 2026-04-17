##DC 
from dash import html, dcc


def _control_group(label, component):
    return html.Div(
        className="control-group",
        children=[
            html.Label(label, className="control-label"),
            component
        ]
    )


def create_layout_dc(meta):
    dc_exclude = {
        "technology",
        "wafer",
        "macro",
        "device",
        "siteX",
        "siteY",
        "Vd",
        "Vg"
    }

    preferred_order = [
        "Id", "Ig",
        "gm", "gds",
        "Cgs", "Cgd", "Cgg",
        "Ft_mean", "Fmax",
        "h21_mag", "h21_dB",
        "S11", "S12", "S21", "S22",
        "S11_dB", "S12_dB", "S21_dB", "S22_dB",
        "Y11_mag", "Y12_mag", "Y21_mag", "Y22_mag",
        "Y11_dB", "Y12_dB", "Y21_dB", "Y22_dB",
    ]

    meta_cols = list(meta.columns)
    dc_params = []

    for p in preferred_order:
        if p in meta_cols and p not in dc_exclude:
            dc_params.append({"label": p, "value": p})

    existing_values = {x["value"] for x in dc_params}
    for p in meta_cols:
        if p not in dc_exclude and p not in existing_values:
            dc_params.append({"label": p, "value": p})

    default_value = []
    for p in ["Id", "gm", "Cgg", "Ft_mean"]:
        if p in meta_cols:
            default_value = [p]
            break

    if not default_value and len(dc_params) > 0:
        default_value = [dc_params[0]["value"]]

    return html.Div(
        className="dashboard-page",
        children=[
            html.Div(
                className="dashboard-shell",
                children=[

                    html.Div(
                        className="tab-content-panel",
                        children=[

                            html.Div(
                                className="panel-title",
                                children="Plot against Gate Bias"
                            ),

                            html.Div(
                                className="control-strip",
                                children=[

                                    _control_group(
                                        "Macro",
                                        dcc.Dropdown(
                                            sorted(meta["macro"].drop_nulls().unique().to_list()) if "macro" in meta.columns else [],
                                            id="dc-macro",
                                            multi=True,
                                            placeholder="Macro"
                                        )
                                    ),

                                    _control_group(
                                        "Device",
                                        dcc.Dropdown(
                                            id="dc-device",
                                            multi=True,
                                            placeholder="Device"
                                        )
                                    ),

                                    _control_group(
                                        "SiteX",
                                        dcc.Dropdown(
                                            id="dc-siteX",
                                            multi=True,
                                            placeholder="SiteX"
                                        )
                                    ),

                                    _control_group(
                                        "SiteY",
                                        dcc.Dropdown(
                                            id="dc-siteY",
                                            multi=True,
                                            placeholder="SiteY"
                                        )
                                    ),

                                    _control_group(
                                        "Vd",
                                        dcc.Dropdown(
                                            id="dc-vd_select",
                                            multi=True,
                                            placeholder="Vd"
                                        )
                                    ),

                                    _control_group(
                                        "Parameter",
                                        dcc.Dropdown(
                                            options=dc_params,
                                            value=default_value,
                                            multi=True,
                                            id="dc-parameter"
                                        )
                                    ),

                                    _control_group(
                                        "X Scale",
                                        dcc.Dropdown(
                                            id="dc-xscale",
                                            options=[
                                                {"label": "X: Linear", "value": "linear"},
                                                {"label": "X: Log", "value": "log"},
                                            ],
                                            value="linear",
                                            clearable=False
                                        )
                                    ),

                                    _control_group(
                                        "Y Scale",
                                        dcc.Dropdown(
                                            id="dc-yscale",
                                            options=[
                                                {"label": "Y: Linear", "value": "linear"},
                                                {"label": "Y: Log", "value": "log"},
                                            ],
                                            value="linear",
                                            clearable=False
                                        )
                                    ),

                                    _control_group(
                                        "Options",
                                        dcc.Checklist(
                                            id="dc-error-toggle",
                                            options=[{"label": " Enable Error Detection", "value": "on"}],
                                            value=["on"]
                                        )
                                    ),
                                ]
                            ),

                            html.Div(
                                className="main-content-grid",
                                children=[

                                    html.Div(
                                        className="plot-panel",
                                        children=[
                                            html.Div(
                                                className="panel-title",
                                                children="Error Debug Panel"
                                            ),
                                            html.Div(
                                                id="dc-debug_panel",
                                                className="validation-box",
                                                children="Run plot to detect issues..."
                                            ),
                                            html.Br(),
                                            html.Div(
                                                className="graph-wrapper",
                                                children=[
                                                    dcc.Graph(
                                                        id="dc-plot",
                                                        style={
                                                            "height": "78vh",
                                                            "width": "100%"
                                                        },
                                                        config={
                                                            "responsive": True,
                                                            "displaylogo": False,
                                                            "toImageButtonOptions": {
                                                                "format": "png",
                                                                "filename": "dc_dashboard_plot",
                                                                "height": 900,
                                                                "width": 1600,
                                                                "scale": 2
                                                            }
                                                        }
                                                    )
                                                ]
                                            )
                                        ]
                                    ),

                                    html.Div(
                                        className="side-stack",
                                        children=[

                                            html.Div(
                                                className="validation-panel",
                                                children=[
                                                    html.Div(
                                                        className="panel-title",
                                                        children="Parameter Validation"
                                                    ),
                                                    html.Div(
                                                        className="panel-subtitle",
                                                        children=(
                                                            "Shows validation only for the selected parameter "
                                                            "(example: gm → gm validation only, gds → gds validation only, "
                                                            "Cgs/Cgd/Cgg → selected capacitance validation only)."
                                                        )
                                                    ),
                                                    html.Div(
                                                        id="dc-validation_output",
                                                        className="validation-box"
                                                    )
                                                ]
                                            ),

                                            html.Div(
                                                className="validation-panel",
                                                children=[
                                                    html.Div(
                                                        className="panel-title",
                                                        children="Error Criteria Validation"
                                                    ),
                                                    html.Div(
                                                        id="dc-error_output",
                                                        className="validation-box"
                                                    )
                                                ]
                                            ),
                                        ]
                                    )
                                ]
                            )
                        ]
                    )
                ]
            )
        ]
    )

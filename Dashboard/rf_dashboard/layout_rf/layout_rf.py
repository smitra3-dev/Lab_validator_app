##RF
from dash import html, dcc


def _control_group(label, component):
    return html.Div(
        className="control-group",
        children=[
            html.Label(label, className="control-label"),
            component
        ]
    )


def create_layout(meta, rf_params):
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
                                children="Plot against Frequency"
                            ),

                            html.Div(
                                className="control-strip",
                                children=[

                                    _control_group(
                                        "Macro",
                                        dcc.Dropdown(
                                            sorted(meta["macro"].drop_nulls().unique().to_list()),
                                            id="rf-macro",
                                            multi=True,
                                            placeholder="Macro"
                                        )
                                    ),

                                    _control_group(
                                        "Device",
                                        dcc.Dropdown(
                                            id="rf-device",
                                            multi=True,
                                            placeholder="Device"
                                        )
                                    ),

                                    _control_group(
                                        "SiteX",
                                        dcc.Dropdown(
                                            id="rf-siteX",
                                            multi=True,
                                            placeholder="SiteX"
                                        )
                                    ),

                                    _control_group(
                                        "SiteY",
                                        dcc.Dropdown(
                                            id="rf-siteY",
                                            multi=True,
                                            placeholder="SiteY"
                                        )
                                    ),

                                    _control_group(
                                        "Vd",
                                        dcc.Dropdown(
                                            id="rf-Vd",
                                            multi=True,
                                            placeholder="Vd"
                                        )
                                    ),

                                    _control_group(
                                        "Vg",
                                        dcc.Dropdown(
                                            id="rf-Vg",
                                            multi=True,
                                            placeholder="Vg"
                                        )
                                    ),

                                    _control_group(
                                        "Parameter",
                                        dcc.Dropdown(
                                            options=[{"label": p, "value": p} for p in rf_params],
                                            value=["S21_dB"],
                                            multi=True,
                                            id="rf-parameter"
                                        )
                                    ),

                                    _control_group(
                                        "X Scale",
                                        dcc.Dropdown(
                                            id="rf-xscale",
                                            options=[
                                                {"label": "X: Linear", "value": "linear"},
                                                {"label": "X: Log", "value": "log"}
                                            ],
                                            value="log",
                                            clearable=False
                                        )
                                    ),

                                    _control_group(
                                        "Y Scale",
                                        dcc.Dropdown(
                                            id="rf-yscale",
                                            options=[
                                                {"label": "Y: Linear", "value": "linear"},
                                                {"label": "Y: Log", "value": "log"}
                                            ],
                                            value="linear",
                                            clearable=False
                                        )
                                    ),

                                    _control_group(
                                        "Options",
                                        dcc.Checklist(
                                            id="rf-error-toggle",
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
                                                id="rf-debug_panel",
                                                className="validation-box",
                                                children="Run plot to detect issues..."
                                            ),
                                            html.Br(),
                                            html.Div(
                                                className="graph-wrapper",
                                                children=[
                                                    dcc.Graph(
                                                        id="rf-plot",
                                                        style={
                                                            "height": "78vh",
                                                            "width": "100%"
                                                        },
                                                        config={
                                                            "responsive": True,
                                                            "displaylogo": False,
                                                            "toImageButtonOptions": {
                                                                "format": "png",
                                                                "filename": "rf_dashboard_plot",
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
                                                        children="Smoothness Validation"
                                                    ),
                                                    html.Div(
                                                        id="rf-validation_output",
                                                        className="validation-box"
                                                    )
                                                ]
                                            ),

                                            html.Div(
                                                className="validation-panel",
                                                children=[
                                                    html.Div(
                                                        className="panel-title",
                                                        children="S-Parameter Screening"
                                                    ),
                                                    html.Div(
                                                        id="rf-sparam_output",
                                                        className="validation-box"
                                                    )
                                                ]
                                            ),

                                            html.Div(
                                                className="validation-panel",
                                                children=[
                                                    html.Div(
                                                        className="panel-title",
                                                        children="h21 Validation"
                                                    ),
                                                    html.Div(
                                                        id="rf-h21_output",
                                                        className="validation-box"
                                                    )
                                                ]
                                            ),

                                            html.Div(
                                                className="validation-panel",
                                                children=[
                                                    html.Div(
                                                        className="panel-title",
                                                        children="Capacitance Validation"
                                                    ),
                                                    html.Div(
                                                        id="rf-cap_output",
                                                        className="validation-box"
                                                    )
                                                ]
                                            ),

                                            html.Div(
                                                className="validation-panel",
                                                children=[
                                                    html.Div(
                                                        className="panel-title",
                                                        children="Ft / Fmax Validation"
                                                    ),
                                                    html.Div(
                                                        id="rf-ftfmax_output",
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

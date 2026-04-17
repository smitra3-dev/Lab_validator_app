##gain 
from dash import html, dcc


def _control_group(label, component):
    return html.Div(
        className="control-group",
        children=[
            html.Label(label, className="control-label"),
            component
        ]
    )


def create_layout_gain(meta):
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
                                children="Gain Bias Dashboard"
                            ),

                            html.Div(
                                className="control-strip",
                                children=[

                                    _control_group(
                                        "Macro",
                                        dcc.Dropdown(
                                            sorted(meta["macro"].drop_nulls().unique().to_list()),
                                            id="gain-macro",
                                            multi=True,
                                            placeholder="Macro"
                                        )
                                    ),

                                    _control_group(
                                        "Device",
                                        dcc.Dropdown(
                                            id="gain-device",
                                            multi=True,
                                            placeholder="Device"
                                        )
                                    ),

                                    _control_group(
                                        "SiteX",
                                        dcc.Dropdown(
                                            id="gain-siteX",
                                            multi=True,
                                            placeholder="SiteX"
                                        )
                                    ),

                                    _control_group(
                                        "SiteY",
                                        dcc.Dropdown(
                                            id="gain-siteY",
                                            multi=True,
                                            placeholder="SiteY"
                                        )
                                    ),

                                    _control_group(
                                        "Vd",
                                        dcc.Dropdown(
                                            id="gain-vd_select",
                                            multi=True,
                                            placeholder="Vd"
                                        )
                                    ),

                                    _control_group(
                                        "Parameter",
                                        dcc.Dropdown(
                                            options=[
                                                {"label": "gm", "value": "gm"},
                                                {"label": "gds", "value": "gds"},
                                                {"label": "Ft_mean", "value": "Ft_mean"},
                                                {"label": "Fmax_mean", "value": "Fmax_mean"},
                                            ],
                                            value=["gm"],
                                            multi=True,
                                            id="gain-parameter"
                                        )
                                    ),

                                    _control_group(
                                        "X Scale",
                                        dcc.Dropdown(
                                            id="gain-xscale",
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
                                            id="gain-yscale",
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
                                            id="gain-error-toggle",
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
                                                id="gain-debug_panel",
                                                className="validation-box",
                                                children="Run plot to detect issues."
                                            ),
                                            html.Br(),
                                            html.Div(
                                                className="graph-wrapper",
                                                children=[
                                                    dcc.Graph(
                                                        id="gain-plot",
                                                        style={
                                                            "height": "78vh",
                                                            "width": "100%"
                                                        },
                                                        config={
                                                            "responsive": True,
                                                            "displaylogo": False,
                                                            "toImageButtonOptions": {
                                                                "format": "png",
                                                                "filename": "gain_dashboard_plot",
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
                                                            "(gm → gm validation only, gds → gds validation only)."
                                                        )
                                                    ),
                                                    html.Div(
                                                        id="gain-validation_output",
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
                                                        id="gain-error_output",
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

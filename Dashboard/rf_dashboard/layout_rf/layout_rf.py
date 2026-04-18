from dash import html, dcc


def _control_group(label, component):
    return html.Div(
        className="control-group",
        children=[
            html.Label(label, className="control-label"),
            component
        ]
    )


def _safe_sorted_unique(meta, col_name):
    if col_name not in meta.columns:
        return []
    values = meta[col_name].drop_nulls().unique().to_list()
    return sorted(values, key=lambda x: str(x))


def create_layout(meta, rf_params):
    macro_values = _safe_sorted_unique(meta, "macro")
    device_values = _safe_sorted_unique(meta, "device")
    sitex_values = _safe_sorted_unique(meta, "siteX")
    sitey_values = _safe_sorted_unique(meta, "siteY")
    vd_values = _safe_sorted_unique(meta, "Vd")
    vg_values = _safe_sorted_unique(meta, "Vg")

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
                                            options=[{"label": str(v), "value": v} for v in macro_values],
                                            value=[macro_values[0]] if macro_values else [],
                                            id="rf-macro",
                                            multi=True,
                                            placeholder="Macro",
                                            clearable=True
                                        )
                                    ),

                                    _control_group(
                                        "Device",
                                        dcc.Dropdown(
                                            options=[{"label": str(v), "value": v} for v in device_values],
                                            value=[],
                                            id="rf-device",
                                            multi=True,
                                            placeholder="Device",
                                            clearable=True
                                        )
                                    ),

                                    _control_group(
                                        "SiteX",
                                        dcc.Dropdown(
                                            options=[{"label": str(v), "value": v} for v in sitex_values],
                                            value=[],
                                            id="rf-siteX",
                                            multi=True,
                                            placeholder="SiteX",
                                            clearable=True
                                        )
                                    ),

                                    _control_group(
                                        "SiteY",
                                        dcc.Dropdown(
                                            options=[{"label": str(v), "value": v} for v in sitey_values],
                                            value=[],
                                            id="rf-siteY",
                                            multi=True,
                                            placeholder="SiteY",
                                            clearable=True
                                        )
                                    ),

                                    _control_group(
                                        "Vd",
                                        dcc.Dropdown(
                                            options=[{"label": str(v), "value": v} for v in vd_values],
                                            value=[],
                                            id="rf-Vd",
                                            multi=True,
                                            placeholder="Vd",
                                            clearable=True
                                        )
                                    ),

                                    _control_group(
                                        "Vg",
                                        dcc.Dropdown(
                                            options=[{"label": str(v), "value": v} for v in vg_values],
                                            value=[],
                                            id="rf-Vg",
                                            multi=True,
                                            placeholder="Vg",
                                            clearable=True
                                        )
                                    ),

                                    _control_group(
                                        "Parameter",
                                        dcc.Dropdown(
                                            options=[{"label": p, "value": p} for p in rf_params],
                                            value=["S21_dB"],
                                            multi=True,
                                            id="rf-parameter",
                                            clearable=True
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
                                                        className="validation-box",
                                                        children="No validation results yet"
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
                                                        className="validation-box",
                                                        children="No S-parameter validation yet"
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
                                                        className="validation-box",
                                                        children="No h21 validation yet"
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
                                                        className="validation-box",
                                                        children="No capacitance validation yet"
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
                                                        className="validation-box",
                                                        children="No Ft/Fmax validation yet"
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
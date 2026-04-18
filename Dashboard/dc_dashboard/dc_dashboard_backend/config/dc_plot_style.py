##dashboard/dc/config/dc_plot_style.py

def apply_dc_figure_layout(fig, valid_params, xscale, yscale, y_title):
    fig.update_layout(
        title={
            "text": f"{y_title} vs Gate Voltage",
            "x": 0.5,
            "xanchor": "center",
            "font": {"size": 20},
        },
        xaxis_title="Gate Voltage Vg (V)",
        yaxis_title=y_title,
        template="simple_white",
        font={"size": 14, "family": "Arial"},
        hovermode="closest",
        plot_bgcolor="white",
        paper_bgcolor="white",
        height=780,
        legend=dict(
            orientation="h",
            yanchor="top",
            y=-0.22,
            xanchor="left",
            x=0.0,
            font=dict(size=10),
            bgcolor="rgba(255,255,255,0.92)",
            bordercolor="rgba(0,0,0,0.15)",
            borderwidth=1,
        ),
        margin=dict(l=70, r=25, t=70, b=170),
    )

    fig.update_xaxes(
        type=xscale,
        showgrid=True,
        gridwidth=1,
        gridcolor="rgba(0,0,0,0.10)",
        zeroline=False,
        showline=True,
        linewidth=1.5,
        linecolor="black",
        mirror=True,
        ticks="outside",
        tickwidth=1.5,
        ticklen=6,
        tickcolor="black",
        title_font=dict(size=16),
        tickfont=dict(size=12),
    )

    fig.update_yaxes(
        type=yscale,
        showgrid=True,
        gridwidth=1,
        gridcolor="rgba(0,0,0,0.10)",
        zeroline=False,
        showline=True,
        linewidth=1.5,
        linecolor="black",
        mirror=True,
        ticks="outside",
        tickwidth=1.5,
        ticklen=6,
        tickcolor="black",
        title_font=dict(size=16),
        tickfont=dict(size=12),
    )

    if len(fig.data) == 0:
        fig.update_layout(title="No plottable data after filtering")

    return fig

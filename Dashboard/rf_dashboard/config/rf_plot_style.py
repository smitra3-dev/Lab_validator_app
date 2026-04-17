##config/rf_plot_style.py
def apply_rf_figure_layout(fig, valid_params, xscale, yscale):
    y_title = ", ".join(valid_params)

    fig.update_layout(
        title={
            "text": f"{', '.join(valid_params)} vs Frequency",
            "x": 0.5,
            "xanchor": "center",
            "font": {"size": 22},
        },
        xaxis_title="Frequency Fs",
        yaxis_title=y_title,
        template="simple_white",
        font=dict(size=15, family="Arial"),
        height=820,
        hovermode="closest",
        plot_bgcolor="white",
        paper_bgcolor="white",
        legend=dict(
            orientation="h",
            yanchor="top",
            y=-0.30,
            xanchor="left",
            x=0.0,
            font=dict(size=11),
            bgcolor="rgba(255,255,255,0.9)",
            bordercolor="black",
            borderwidth=1,
            itemwidth=90,
        ),
        margin=dict(l=85, r=35, t=80, b=230),
    )

    fig.update_xaxes(
        type=xscale,
        showgrid=True,
        gridwidth=1,
        gridcolor="rgba(0,0,0,0.12)",
        zeroline=False,
        showline=True,
        linewidth=2,
        linecolor="black",
        mirror=True,
        ticks="outside",
        tickwidth=2,
        ticklen=6,
        tickcolor="black",
        minor=dict(
            showgrid=True,
            gridwidth=0.5,
            gridcolor="rgba(0,0,0,0.06)",
            ticks="outside",
        ),
        title_font=dict(size=18),
        tickfont=dict(size=13),
    )

    fig.update_yaxes(
        type=yscale,
        showgrid=True,
        gridwidth=1,
        gridcolor="rgba(0,0,0,0.12)",
        zeroline=False,
        showline=True,
        linewidth=2,
        linecolor="black",
        mirror=True,
        ticks="outside",
        tickwidth=2,
        ticklen=6,
        tickcolor="black",
        minor=dict(
            showgrid=True,
            gridwidth=0.5,
            gridcolor="rgba(0,0,0,0.06)",
            ticks="outside",
        ),
        title_font=dict(size=18),
        tickfont=dict(size=13),
    )

    if len(fig.data) == 0:
        fig.update_layout(title="⚠ No plottable data after scale filtering")

    return fig

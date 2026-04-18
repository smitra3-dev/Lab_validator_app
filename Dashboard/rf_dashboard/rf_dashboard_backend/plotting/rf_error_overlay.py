##plotting/rf_error_overlay.py
from dash import html
import plotly.graph_objects as go

from validation.Anomaly_predictor.anomaly_detector.rf_anomaly_detector import detect_rf_anomalies

def add_rf_error_overlays(fig, group, param, trend_debug_logs):
    try:
        result_df, debug_log = detect_rf_anomalies(group, "Fs", param)
        trend_debug_logs.extend(debug_log)

        red_df = result_df[result_df["label"] == "red"]
        if not red_df.empty:
            fig.add_trace(go.Scatter(
                x=red_df["Fs"],
                y=red_df[param],
                mode="markers",
                marker=dict(
                    symbol="circle-cross",
                    size=11,
                    color="red",
                    line=dict(width=1, color="black"),
                ),
                name=f"{param} error",
                showlegend=False,
                hovertemplate="Fs=%{x:.4g}<br>Value=%{y:.4e}<extra>Error</extra>",
            ))

        yellow_df = result_df[result_df["label"] == "yellow"]
        if not yellow_df.empty:
            fig.add_trace(go.Scatter(
                x=yellow_df["Fs"],
                y=yellow_df[param],
                mode="markers",
                marker=dict(
                    symbol="circle",
                    size=9,
                    color="yellow",
                    line=dict(width=1, color="black"),
                ),
                name=f"{param} warning",
                showlegend=False,
                hovertemplate="Fs=%{x:.4g}<br>Value=%{y:.4e}<extra>Warning</extra>",
            ))
    except Exception as e:
        trend_debug_logs.append(f"[ENGINE ERROR] {param}: {str(e)}")


def build_rf_debug_children(error_detection_on, trend_debug_logs):
    if error_detection_on:
        return [
            html.Div(log, style={"color": "#00FFAA", "fontSize": "11px"})
            for log in trend_debug_logs
        ] or [html.Div("No errors detected", style={"color": "#00FFAA", "fontSize": "11px"})]

    return [html.Div("Error detection is OFF", style={"color": "#AAAAAA", "fontSize": "11px"})]

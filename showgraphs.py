import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from scipy import signal


def draw_graph():
    hr_df = pd.read_csv("hrdata.csv")

    steps_df = pd.read_csv("stepsdata.csv")

    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Scatter(
        x=hr_df.Date,
        y=hr_df['Heartrate'],
        mode='markers',
        marker=dict(size=2, color='lightskyblue'),
        name="Raw heart rate",
        opacity=0.8), secondary_y=True, )

    fig.add_trace(go.Scatter(
        x=hr_df.Date,
        y=signal.savgol_filter(hr_df['Heartrate'],
                               53,  # window size used for filtering
                               3),  # order of fitted polynomial,
        name="Heart rate",
        line_color='deepskyblue',
        opacity=0.8), secondary_y=True, )

    fig.add_trace(go.Scatter(
        x=steps_df.Date,
        y=steps_df['Steps'],
        name="Steps",
        line_color='dimgray',
        opacity=0.8), secondary_y=False, )

    # Set x-axis title
    fig.update_xaxes(title_text="<b>Timeline</b>")

    # Set y-axes titles
    fig.update_yaxes(title_text="<b>Heart rate</b>", secondary_y=False)
    fig.update_yaxes(title_text="<b>Steps</b>", secondary_y=True)

    fig.update_layout(title_text='Heart rate with steps.',
                      xaxis_rangeslider_visible=True)

    fig.show()

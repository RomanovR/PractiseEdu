import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

hrDf = pd.read_csv("hrdata_middle.csv")

stepsDf = pd.read_csv("stepsdata.csv")


fig = make_subplots(specs=[[{"secondary_y": True}]])
fig.add_trace(go.Scatter(
    x=hrDf.Date,
    y=hrDf['Heartrate'],
    name="Heart rate",
    line_color='deepskyblue',
    opacity=0.8), secondary_y=True, )

fig.add_trace(go.Scatter(
    x=stepsDf.Date,
    y=stepsDf['Steps'],
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

import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("data/timeline.csv")

fig = go.Figure()

# Add traces with visible setting
fig.add_trace(go.Scatter(x=df['time'], y=df['no trains'], name='no trains', visible='legendonly'))
fig.add_trace(go.Scatter(x=df['time'], y=df['no on time'], name='no on time', visible='legendonly'))
fig.add_trace(go.Scatter(x=df['time'], y=df['up to 6'], name='up to 6', visible=True))
fig.add_trace(go.Scatter(x=df['time'], y=df['up to 60'], name='up to 60', visible=True))
fig.add_trace(go.Scatter(x=df['time'], y=df['up to 120'], name='up to 120', visible=True))
fig.add_trace(go.Scatter(x=df['time'], y=df['Over 120'], name='Over 120', visible=True))

fig.update_layout(width=800)
fig.show()
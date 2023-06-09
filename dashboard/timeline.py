import pandas as pd
import plotly.graph_objects as go
import pyodide
raw_path='https://raw.githubusercontent.com/adammielniczuk/dash/main/dashboard/data'

df = pd.read_csv(pyodide.http.open_url(raw_path+"/timeline.csv"))

timeline = go.Figure()

# Add traces with visible setting
timeline.add_trace(go.Scatter(x=df['time'], y=df['no trains'], name='total no. of trains', visible='legendonly'))
timeline.add_trace(go.Scatter(x=df['time'], y=df['no on time'], name='no. of traind on time', visible='legendonly'))
timeline.add_trace(go.Scatter(x=df['time'], y=df['up to 6'], name='up to 6 minutes late', visible=True))
timeline.add_trace(go.Scatter(x=df['time'], y=df['up to 60'], name='up to 60 minutes late', visible=True))
timeline.add_trace(go.Scatter(x=df['time'], y=df['up to 120'], name='up to 120 minutes late', visible=True))
timeline.add_trace(go.Scatter(x=df['time'], y=df['Over 120'], name='Over 120 minutes late', visible=True))

timeline.update_layout(height=370, margin=dict(t=10,b=10,r=10, l=10), font={'family':'Segoe UI', 'size':15})

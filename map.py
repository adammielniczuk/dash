import plotly.graph_objects as go
from PIL import Image
import pandas as pd

img = Image.open('map.png')

i_x, i_y = img.size

cities_coordinates = pd.read_csv("cities.csv")
cities_coordinates["Latitude"] = cities_coordinates["Latitude"].apply(lambda x : (x - 48.84) / (55.32 - 48.84))
cities_coordinates["Longitude"] = cities_coordinates["Longitude"].apply(lambda x : (x - 13.50) / (24.80 - 13.50))

late_times = pd.read_csv("city_late.csv", sep=";")
late_times = late_times.sort_values('station')
late_times = late_times.set_index('station')

stations = late_times.index.to_list()

# Create the data for the pie charts
labels = ['On Time', 'Late']

traces = []
for index, row in cities_coordinates.iterrows():
    value = late_times.iloc[index]["january"]
    trace = go.Pie(
        labels=labels,
        values=[value, 1-value],
        domain=dict(x=[row['Longitude']-0.05, row['Longitude']+0.05], y=[row['Latitude']-0.05, row['Latitude']+0.05]),
        name=stations[index]
    )
    traces.append(trace)

# Create the layout for the chart with a custom CSS background
layout = go.Layout(
    title='Percent of late trains for a given mounth',
    xaxis=dict(visible=False),
    yaxis=dict(visible=False),
    autosize=False,
    width=i_x,
    height=i_y,
    margin=dict(l=0, r=0, t=30, b=0)
)

# Create the figure and add the traces and layout
map_fig = go.Figure(data=traces, layout=layout)

# Add a custom background image using CSS
map_fig.update_layout(
    images=[
        go.layout.Image(
            source=img,
            xref="paper",
            yref="paper",
            x=0,
            y=1,
            sizex=1,
            sizey=1,
            sizing="stretch",
            opacity=1,
            layer="below"
        )
    ]
)

# Define the steps for the slider
steps = []
for column in late_times.columns:
    values = [[i, 1-i] for i in late_times[column].tolist()]
    step = dict(
        method="update",
        args=[{"values": values}],
        label=column
    )
    steps.append(step)

# Add the slider to the figure
map_fig.update_layout(
    sliders=[
        go.layout.Slider(
            active=0,
            currentvalue={"prefix": "Month: "},
            steps=steps
        )
    ]
)


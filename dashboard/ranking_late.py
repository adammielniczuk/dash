import plotly.graph_objects as go
import pandas as pd

import pyodide
raw_path='https://raw.githubusercontent.com/adammielniczuk/dash/main/dashboard/data'

df = pd.read_csv(pyodide.http.open_url(raw_path+"/companies_late.csv"))

images = []

fig_late = go.Figure()

def create_plot(attribute, visible = False):
    df_teporary = df.sort_values(attribute, ascending=True)
    df_teporary = df_teporary.reset_index(drop=True)

    for index, row in df_teporary.iterrows():
        im = raw_path+ row["Logo_Path"][4:]
        size_factor = df_teporary.shape[0]
        pozition_factor = df_teporary[attribute].max()
        images.append(
            dict(
                source=im,
                xref="paper",  # x-axis reference is relative to the plot area
                yref="paper",  # y-axis reference is relative to the plot area
                x=(row[attribute])  / pozition_factor,  # x-coordinate of the image
                y= (index +1)/size_factor,  # y-coordinate of the image
                sizex=1/size_factor,  # size of the image on the x-axis
                sizey=1/size_factor,  # size of the image on the y-axis
                sizing="stretch",  # image sizing mode
                opacity=0.8,  # image opacity (adjust as needed)
                layer="above",  # image layer position is below the bars
                visible = visible
            )
        )
    fig_late.add_trace(go.Bar(
    y=df_teporary['Company'],  # Swap x and y
    x=df_teporary[attribute],  # Swap x and y
    name=attribute,
    marker_color=df_teporary['colors'],
    orientation='h',  # Set orientation to 'h' for horizontal chart
    visible=visible,
    hovertemplate="%{x} %{y}<extra></extra>"
))
    
create_plot('Late_Percent', visible=True)
create_plot('late_trains')
create_plot('late_total_time')



fig_late.update_layout(
    title='',
    xaxis=dict(title=''),  # Swap x and y axis titles
    yaxis=dict(title=''),  # Swap x and y axis titles
    barmode='group',
    plot_bgcolor='rgba(0, 0, 0, 0)',
    images = images,
    margin=dict(t=10,b=10,r=10, l=10), font={'family':'Segoe UI', 'size':15}
)



viz_images1 = dict()
viz_images2 = dict()
viz_images3 = dict()
for i in range(len(images)):
    if i < len(images) / 3:
        viz_images1[f"images[{i}].visible"] = True
        viz_images2[f"images[{i}].visible"] = False
        viz_images3[f"images[{i}].visible"] = False
    elif i < len(images) *2 / 3:
        viz_images1[f"images[{i}].visible"] = False
        viz_images2[f"images[{i}].visible"] = True
        viz_images3[f"images[{i}].visible"] = False
    else:
        viz_images1[f"images[{i}].visible"] = False
        viz_images2[f"images[{i}].visible"] = False
        viz_images3[f"images[{i}].visible"] = True



# Define dropdown menu
updatemenu = [
    {
        'buttons': [
            {'label': 'Percent on time', 'method': 'update', 'args': [{'visible': [True, False, False]}, viz_images1]},
            {'label': 'Number of late trains', 'method': 'update', 'args': [{'visible': [False, True, False]}, viz_images2]},
            {'label': 'Total delay time', 'method': 'update', 'args': [{'visible': [False, False, True]}, viz_images3]}
        ],
        'direction': 'down',
        'showactive': True,
        'x':0,
        'y':1.15
    }
]

# Add dropdown menu to the layout
fig_late.update_layout(showlegend=False, updatemenus=updatemenu)


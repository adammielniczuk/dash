import plotly.graph_objects as go
import pandas as pd

raw_path='https://raw.githubusercontent.com/adammielniczuk/dash/main/dashboard/data'

df = pd.read_csv(raw_path+"/delay_reasons.csv")
df = df.set_index('reason')

df_infrastructure = pd.read_csv(raw_path+"/infrastructure.csv")
df_infrastructure = df_infrastructure.set_index('reason')

df_logistics = pd.read_csv(raw_path+"/logistics.csv")
df_logistics = df_logistics.set_index('reason')

df_weather = pd.read_csv(raw_path+"/weather.csv")
df_weather =df_weather.set_index('reason')

df_crime = pd.read_csv(raw_path+"/crime.csv")
df_crime = df_crime.set_index('reason')

all_df = [df, df_infrastructure, df_logistics, df_weather, df_crime]
visible =[] * len(all_df)
print(visible)

for i in range(len(all_df)):
    visible.append(list())

for i in range(len(all_df)):
    for j in range(len(all_df)):
        visible[j] += ([i == j] * all_df[i].shape[0])

 




layout = go.Layout(
    title='Stacked Bar Chart',
    barmode='stack',
    updatemenus=[
        dict(
            buttons=list([
                dict(
                    label='Overview',
                    method='update',
                    args=[{'visible': visible[0]}, {'title': 'Chart 1'}]
                ),
                dict(
                    label='Infrastructure',
                    method='update',
                    args=[{'visible': visible[1]}, {'title': 'Chart 2'}]
                ),
                dict(
                    label='Logistics',
                    method='update',
                    args=[{'visible': visible[2]}, {'title': 'Chart 2'}]
                ),
                dict(
                    label='Weather',
                    method='update',
                    args=[{'visible': visible[3]}, {'title': 'Chart 2'}]
                ),
                dict(
                    label='Crime and accidents',
                    method='update',
                    args=[{'visible': visible[4]}, {'title': 'Chart 2'}]
                ),
            ]),
            direction='down',
            showactive=True,
            x=0.1,
            xanchor='left',
            y=1.2,
            yanchor='top'
        ),
    ]
)


fig = go.Figure(layout=layout)

def create_plot(df, visible = False):    
    for index, data in df.iterrows():
        fig.add_trace(
            go.Bar(
                x = df.columns, 
                y = data, 
                name=index,
                visible=visible
            )
        )

create_plot(df, visible=True)
for df in all_df[1:]:
    create_plot(df)





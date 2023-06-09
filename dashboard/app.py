from shiny import App, render, ui
import os

from shinywidgets import output_widget, render_widget
import plotly.graph_objects as go
import plotly.io as pio
from map import map_fig
from delay_reasons import fig
from timeline import timeline


app_ui = ui.page_fluid(
    ui.h3("How late are polish trains?"),
    ui.layout_sidebar(
        ui.panel_sidebar(
            output_widget("timeline_plot")
        )
    ),
    ui.panel_main(
        ui.div(
            ui.h5('graph'),
            output_widget("plot")
        )
    )

)


def server(input, output, session):
    @output
    @render.text
    def txt():
        return f"n*2 is {input.n() * 2}"
    
    
    @output
    @render_widget
    def plot():       
        return fig  
    
    @output
    @render_widget
    def timeline_plot():       
        return timeline

app = App(app_ui, server)


if __name__ == '__main__':
    app.run()

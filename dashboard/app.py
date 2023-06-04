from shiny import App, render, ui
import pyodide

pyodide.loadPackage('shinywidgets')
from shinywidgets import output_widget, render_widget
import plotly.graph_objects as go
import plotly.io as pio
from map import map_fig



app_ui = ui.page_fluid(
    ui.h2("Hello akadsubbhjkdcvbmhdsf!"),
    ui.input_slider("n", "N", 0, 100, 20),
    ui.output_text_verbatim("txt"),
    output_widget("plot")
)


def server(input, output, session):
    @output
    @render.text
    def txt():
        return f"n*2 is {input.n() * 2}"
    
    
    @output
    @render_widget
    def plot():       
        return map_fig  
    


app = App(app_ui, server)

if __name__ == '__main__':
    app.run()

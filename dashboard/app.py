from shiny import App, render, ui
from shinywidgets import output_widget, render_widget
import plotly.graph_objects as go
import plotly.io as pio
from map import map_fig
from delay_reasons import fig
from timeline import timeline
from ranking_work import fig_rank
from ranking_late import fig_late
app_ui = ui.page_fluid(
   # shinyswatch.theme.darkly(),
    ui.h3("How late are polish trains?"),
    
    ui.layout_sidebar(
        ui.panel_sidebar(
            {'style':'background-color: rgba(255,255,255,0)'},
            ui.h5({'class':'card-title mt-0'}, 'graph'),
            output_widget("map_plot"),
            
            ),
        ui.panel_main(
            ui.navset_pill_card(
                ui.nav("The reasons of the delays in different months",
                    {'class': "card-body"},
        
                    output_widget("plot"),
                    
                ),
                ui.nav("Biggest train companies by workload statistics",
                    {'class': "card-body"},
                    
                    output_widget("work_plot"),
                    
                ),
            ),
             ui.navset_pill_card(
                ui.nav("Number of late trains over time",
                    {'class': "card-body"},

                    output_widget("timeline_plot"),
                    
                ),
                ui.nav("Ranking of train lateness by company",
                    {'class': "card-body"},

                    output_widget("late_plot"),
                    
                ),
            ),
            
        ),   
        

    )
) 


def server(input, output, session):
    @output
    @render.text
    def txt():
        return f"n*2 is 2"
    @output
    @render.image
    def img():
        return 'C:\\Users\\creep\\Desktop\\studia\\sem4\\dashboard\\dashboard\\data\\pp.png'
    
    @output
    @render_widget
    def plot():       
        return fig 
    
    @output
    @render_widget
    def timeline_plot():       
        return timeline
    @output
    @render_widget
    def map_plot():       
        return map_fig
    @output
    @render_widget
    def work_plot():       
        return fig_rank
    @output
    @render_widget
    def late_plot():       
        return fig_late

app = App(app_ui, server)


if __name__ == '__main__':
    app.run()

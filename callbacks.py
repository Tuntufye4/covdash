import plotly.express as px
from dash import Input, Output
from data import covid_data

def update_charts(selected_filter):
    if selected_filter == 'OnTreatment':
        bar_chart_data = px.bar(x=covid_data['District'], y=covid_data['OnTreatment'], labels={'x': 'District', 'y': 'On Treatment'})
        pie_chart_data = px.pie(names=covid_data['District'], values=covid_data['OnTreatment'], title=f'COVID-19 {selected_filter} Distribution')
    else:
        bar_chart_data = px.bar(x=covid_data['District'], y=covid_data['Vaccinated'], labels={'x': 'District', 'y': 'Vaccinated'})
        pie_chart_data = px.pie(names=covid_data['District'], values=covid_data['Vaccinated'], title=f'COVID-19 {selected_filter} Distribution')

    return bar_chart_data, pie_chart_data

def register_callbacks(app):
    @app.callback(
        [Output('bar-chart', 'figure'),
         Output('pie-chart', 'figure')],
        [Input('chart-filter', 'value')]
    )
    def update_charts_callback(selected_filter):
        return update_charts(selected_filter)

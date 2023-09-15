import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
import plotly.graph_objs as go
import dash_leaflet as dl

# Sample COVID-19 data
covid_data = {
    "District": ["Lilongwe", "Blantyre", "Mzuzu", "Zomba", "Dedza"],
    "Cases": [100, 50, 200, 75, 120],
    "Latitude": [-13.9833, -15.7833, -11.4655, -15.3833, -14.3667],
    "Longitude": [33.7833, 35.0000, 34.0209, 35.3167, 34.3333]
}

# Create the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="#")),
        dbc.NavItem(dbc.NavLink("About", href="#")),
        dbc.NavItem(dbc.NavLink("Contact", href="#")),
    ],
    brand="COVID-19 Dashboard",
    brand_href="#",
    color="dark",
    dark=True,
)

app.layout = html.Div([
    navbar,
    html.H1("COVID-19 Statistics"),
    
    # Bar Graph
    html.Div([
        dcc.Graph(
            id='bar-graph',
            figure={
                'data': [go.Bar(x=covid_data['District'], y=covid_data['Cases'])],
                'layout': {'title': 'COVID-19 Cases by District'}
            }
        )
    ], style={'display': 'inline-block', 'width': '45%'}),
    
    # Count Number
    html.Div([
        html.H2("Total COVID-19 Cases"),
        html.H3(sum(covid_data['Cases']), style={'font-size': '36px', 'margin-right': '150px'})
    ], style={'display': 'inline-block', 'width': '45%', 'vertical-align': 'top', 'margin-top': '20px'}),
    
    # Left Section: Pie Chart
    html.Div([
        dcc.Graph(
            id='pie-chart',
            figure={
                'data': [go.Pie(labels=covid_data['District'], values=covid_data['Cases'])],
                'layout': {'title': 'COVID-19 Cases Distribution'}
            }
        )
    ], style={'display': 'inline-block', 'width': '45%'}),
    
    # Right Section: Dash Leaflet Map with Markers
    html.Div([
        dl.Map([
            dl.TileLayer(),
            *[
                dl.Marker(position=(lat, lon), children=[
                    dl.Tooltip(f"District: {district}<br>Cases: {cases}")
                ]) for district, cases, lat, lon in zip(covid_data['District'], covid_data['Cases'], covid_data['Latitude'], covid_data['Longitude'])
            ]
        ], center=(-13.254308, 34.301525), zoom=6, style={'width': '100%', 'height': '400px'}),
    ], style={'display': 'inline-block', 'width': '55%', 'vertical-align': 'top'}),
])

if __name__ == '__main__':
    app.run_server(debug=False)



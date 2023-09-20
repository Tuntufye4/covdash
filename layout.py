from dash import html, dcc
import dash_bootstrap_components as dbc
from styles import card_styles
from data import covid_data


def create_layout():
    layout = html.Div([
        # Title and Line Section
        html.Div([
            html.H1("COVID-19 Statistics", style={'margin-top': '20px', 'margin-left': '115px'}),
            html.Hr(style={'border-top': '2px solid #ccc', 'margin-left': '115px', 'margin-right': '230px'}),
        ]),
        
        # Cards Section
        dbc.Row([
            # Total Cases Card
            dbc.Col(
                dbc.Card(
                    dbc.CardBody([
                        html.H3(sum(covid_data['Cases']), className="card-count"),
                        html.P("Total COVID-19 Cases", className="card-text"),
                    ]),
                    color=card_styles["light"]
                ),
                width={"size": 3, "offset": 1},
            ),
            
            # Vaccinated Card
            dbc.Col(
                dbc.Card(
                    dbc.CardBody([
                        html.H3(sum(covid_data['Vaccinated']), className="card-count text-white"),
                        html.P("Count of Vaccinated", className="card-text text-white"),
                    ]),
                    color=card_styles["dark"]
                ),
                width={"size": 3},
            ),
            
            # On Treatment Card
            dbc.Col(
                dbc.Card(
                    dbc.CardBody([
                        html.H3(sum(covid_data['OnTreatment']), className="card-count text-white"),
                        html.P("Count of Those on Treatment", className="card-text text-white"),
                    ]),
                    color=card_styles["primary"]
                ),
                width={"size": 3},
            ),
        ], style={'margin-top': '20px', 'margin-bottom': '30px'}),
        
        # Dropdowns Section
        dbc.Row([
            # Dropdown for Chart Filter (centered)
            dbc.Col(
                dcc.Dropdown(
                    id='chart-filter',
                    options=[
                        {'label': 'On Treatment', 'value': 'OnTreatment'},
                        {'label': 'Vaccinated', 'value': 'Vaccinated'}
                    ],
                    value='OnTreatment',
                ),
                width={"size": 6, "offset": 3},
            ),
        ], style={'margin-top': '20px'}),
        
        # Charts Section (side by side)
        dbc.Row([
            # Left Section: Bar Graph
            dbc.Col(
                dcc.Graph(
                    id='bar-chart',
                    config={'displayModeBar': False},  # Hide the mode bar
                    style={'width': '100%', 'height': '400px'}  # Adjust the height as needed
                ),
                width=6,
            ),
            
            # Right Section: Pie Chart
            dbc.Col(
                dcc.Graph(
                    id='pie-chart',
                    config={'displayModeBar': False},  # Hide the mode bar
                    style={'width': '100%', 'height': '400px'}  # Adjust the height as needed
                ),
                width=6,
            ),
        ]),
    ])
    
    return layout

from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go

# Sample data
categories = ['Languages', 'Mathematics & Sciences', 'Social Studies', 'Creative Arts', 'Technology', 'Religious and Ethical Education', ' Business and Economics']
values = [4, 7, 2, 5, 6, 9, 8]

# Build Dash App
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Layout
def example_radar_chart():
    radar = dbc.Card([
        dbc.CardHeader("Current Stats"),
        dcc.Graph(
            id='radar-chart',
            figure={
                'data': [
                    go.Scatterpolar(
                        r=values,
                        theta=categories,
                        fill='toself',
                        name='Radar Chart'
                    ),
                ],
                'layout': go.Layout(
                    polar=dict(
                        radialaxis=dict(
                            visible=True,
                            range=[0, 10]
                        )
                    ),
                    showlegend=True,
                )
            },
            style={'height': '410px'}
        ),
    ]
    )

    return radar

import dash_bootstrap_components as dbc
from dash import html

def example_card(header, text):
    cards = dbc.Card([
        dbc.CardHeader(header),
        dbc.CardBody(
            [
                html.P(text, style={"margin": "0"})
            ]
        ),
    ])
    return cards
from dash import Dash, html, dcc, register_page
import dash_bootstrap_components as dbc

import plotly.express as px
import pandas as pd

df = pd.DataFrame(dict(
    r=[0, 2, 1, 4, 0],
    skills=["skill a", "skill b", "skill c", "skill d", "skill e"]))

fig = px.line_polar(df, r='r', theta='skills', line_close=True)

register_page(__name__)

layout = dbc.Card(
    dbc.CardBody(
        [
            html.P("Here are your skills:"),
            dcc.Graph(figure=fig),
        ],
        style={"display": "flex", "justify-content": "center", "align-items": "center", "flex-direction": "column"}
    ),
)
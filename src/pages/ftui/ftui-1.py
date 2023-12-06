from dash import Dash, html, dcc, register_page
import dash_bootstrap_components as dbc

import plotly.express as px
import pandas as pd

df = pd.DataFrame(dict(
    r=[0, 0, 0, 0, 0],
    skills=["skill a", "skill b", "skill c", "skill d", "skill e"]))

fig = px.line_polar(df, r='r', theta='skills', line_close=True)

register_page(__name__)

layout = html.Div(
    [
        dbc.Card(
            dbc.CardBody(
                [
                    html.P("What fields are you interested in?", style={"marginBottom": "-10vh", "zIndex": "999", "color": "#666", "fontSize": "2em"}),
                    html.Img(src="/assets/images/factory.jpg", style={"width": "80%", "marginBottom": "-10vh", "marginTop": "-10vh"}),
                    html.Div(
                        dcc.Dropdown(
                            [
                                "Technology",
                                "Healthcare",
                                "Finance",
                                "Education",
                            ],
                            multi=True,
                            style={"width": "100%"}
                        ),
                        style={"width": "50%", "marginTop": "-15vh"}
                    ),
                ],
                style={
                    "display": "flex",
                    "justify-content": "space-evenly",
                    "align-items": "center",
                    "flex-direction": "column",
                    "width": "45vw",
                    "height": "90vh",
                }
            )
        ),
        dbc.Card(
            dbc.CardBody(
                [
                    html.P("What jobs are you interested in?", style={"marginBottom": "-20vh", "zIndex": "999", "color": "#666", "fontSize": "2em"}),
                    html.Img(src="/assets/images/job.jpg", style={"width": "50%", "marginBottom": "-5vh", "marginTop": "-5vh"}),
                    html.Div(
                        dcc.Dropdown(
                            [
                                "Software Developer",
                                "Data Scientist",
                                "Network Engineer",
                                "Cybersecurity Analyst",
                                "UI/UX Designer",
                                "Hardware Engineer",
                                "System Administrator",
                                "IT Support Specialist"
                            ],
                            multi=True,
                            style={"width": "100%"}
                        ),
                        style={"width": "50%", "marginTop": "-15vh"}
                    ),
                ],
                style={
                    "display": "flex",
                    "justify-content": "space-around",
                    "align-items": "center",
                    "flex-direction": "column",
                    "width": "45vw",
                    "height": "90vh",
                }
            )
        ),
        html.A(
            dbc.Button(
                "Next",
                color="success",
                className="mr-1",
                style={
                    "width": "5vw",
                }
            ), 
            href="/ftui/ftui-2", 
            style={
                "position": "fixed",
                "bottom": "2vh",
                "right": "3vw",
            }
        ),
    ],
    style={
        "marginTop": "2vh",
        "height": "90vh",
        "width": "99vw",
        "display": "flex",
        "justify-content": "space-evenly",
        "align-items": "center",
    }
)

# layout = html.Div([
#     dbc.Card(
#         dbc.CardBody(
#             [
#                 html.H2("What fields are you interested in?"),
#                 html.Div(
#                     dcc.Dropdown(
#                         [
#                             "Technology",
#                             "Healthcare",
#                             "Finance",
#                             "Education",
#                         ],
#                         multi=True,
#                         style={"width": "100%"}
#                     ),
#                     style={"width": "50%"}
#                 ),
#             ],
#             style={"display": "flex", "justify-content": "center", "align-items": "center", "flex-direction": "column"}
#         ),
#         style={"marginTop": "2vh"}
#     ),
#     dbc.Card(
#         dbc.CardBody(
#             [
#                 html.H2("What jobs are you interested in?"),
#                 html.Div(
#                     dcc.Dropdown(
#                         [
#                             "Software Developer",
#                             "Data Scientist",
#                             "Network Engineer",
#                             "Cybersecurity Analyst",
#                             "UI/UX Designer",
#                             "Hardware Engineer",
#                             "System Administrator",
#                             "IT Support Specialist"
#                         ],
#                         style={"width": "100%"}
#                     ),
#                     style={"width": "50%"}
#                 ),
#             ],
#             style={"display": "flex", "justify-content": "center", "align-items": "center", "flex-direction": "column"}
#         ),
#         style={"marginTop": "2vh"}
#     ), 
#     dbc.Card(
#         dbc.CardBody(
#             [
#                 html.P("Let's see how your skills do with a baseline quiz."),
#                 html.A(dbc.Button("Let's go!", color="primary", className="mr-1"), href="/ftui/ftui-2"),
#             ],
#             style={"display": "flex", "justify-content": "center", "align-items": "center", "flex-direction": "column"}
#         ),
#         style={"marginTop": "2vh"}
#     ), 
# ])
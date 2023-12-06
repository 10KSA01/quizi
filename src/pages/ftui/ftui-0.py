from dash import Dash, html, dcc, register_page
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import json
import platform

file_path = ""
if platform.system() == 'Windows':
    file_path = "app/data/skills.json"
else:
    file_path = "data/skills.json"
    
with open(file_path, 'r') as file:
    skills_data = json.load(file)

skills_list = list(skills_data['MainSkills'].keys())

skill_levels = []
for skill in skills_data['MainSkills']:
    skill_levels.append(0)

df = pd.DataFrame(dict(
    level=skill_levels,
    skills=skills_list))

fig = px.line_polar(df, r='level', theta='skills', line_close=True)

register_page(__name__)

layout = html.Div(
    [
        html.H1("Welcome, Yusif!", style={"color": "#333"}),
        html.Div([
                html.Img(src="/assets/images/profile-pic.jpg", style={"width": "70%"}),
                html.P("Newbie", style={"color": "#aaa", "marginTop": "-1vh"}),
            ],
            style={"display": "flex", "justify-content": "center", "align-items": "center", "flex-direction": "column"}
        ),
        html.P("Let's get started. Your skills are going to look like this:", style={"fontSize": "1.5rem", "color": "#333"}),
        html.Div([
            dcc.Graph(figure=fig, style={"width": "50vw"}),
        ],
        style={
            "width": "60%", 
            "display": "flex", 
            "justify-content": "space-evenly", 
            "align-items": "center", 
            "flex-direction": "row",
        }),
        html.P("Let's add some lines. Are you ready?", style={"fontSize": "1.5rem", "color": "#333"}),
        html.A(dbc.Button("Let's go!", color="primary", className="mr-1"), href="/ftui/ftui-1"),
    ],
    style={"display": "flex", "justify-content": "center", "align-items": "center", "flex-direction": "column", "height": "95vh", "outline": "1px solid #333"}
)
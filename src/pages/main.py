from dash import Dash, html, dcc, register_page
import dash_bootstrap_components as dbc
from components.Charts import *
from components.Tables import *
from components.MiniCards import *
from components.Items import example_daily_item
import random
import platform
import json
import plotly.express as px


register_page(__name__, path='/')

file_path = "app/data/skills.json" if platform.system() == 'Windows' else "data/skills.json"

with open(file_path, 'r') as file:
    skills_data = json.load(file)

skills_list = list(skills_data['MainSkills'].keys())

skill_levels = []
dream_job_skill_levels = []
for skill in skills_data['MainSkills']:
    skill_levels.append(random.randint(0, 10))
    dream_job_skill_levels.append(random.randint(10, 20))

df1 = pd.DataFrame(dict(
    level=skill_levels,
    skills=skills_list,
))

df2 = pd.DataFrame(dict(
    level=dream_job_skill_levels,
    skills=skills_list,
))

df1['Type'] = 'You'
df2['Type'] = 'Software Engineer'

df = pd.concat([df1, df2], ignore_index=True)

fig = px.line_polar(df, r='level', theta='skills', color="Type", line_close=True)

layout = dbc.CardBody(
    style={
        "padding": "0vh 1vw",
    },
    children=[
        html.Br(),
        dbc.Row([
                dbc.Col([   
                    dbc.Card([
                        dbc.CardHeader("Your Stats", style={"fontSize": "1.2em"}),
                        dcc.Graph(
                            figure=fig,
                            style={'width': '100%'}
                    )
                    ]),
                    ], width=6),
                dbc.Col([example_activity_friends()], width=6),
            ],
            align="center",
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col([example_daily_item("Day 1", "+15 points", True)], width={"size": 2}),
                dbc.Col([example_daily_item("Day 2", "+15 points", True)], width={"size": 2}),
                dbc.Col([example_daily_item("Day 3", "+20 points", True)], width={"size": 2}),
                dbc.Col([example_daily_item("Day 4", "New Title: Beginner", False)], width={"size": 2}),
                dbc.Col([example_daily_item("Day 5", "New Title: Hard Worker", False)], width={"size": 2}),
                dbc.Col([example_daily_item("Day 6", "+15 points", False)], width={"size": 2}),
                dbc.Col([example_daily_item("Day 7", "New Title: Weekly Challenge", False)], width={"size": 2}),
            ],
            className="overflow-auto",
            style={"flex-wrap": "nowrap"}
        ),
        html.Br(),
        dbc.Row(
            style={
                "padding": "0vh 0.5vw",
            },
            children=[
                dbc.Card(
                    [
                        dbc.CardHeader("Recommendations", style={"fontSize": "1.2em"}),
                        dbc.CardBody(
                            [
                                dbc.Row([
                                    dbc.Col([
                                    dbc.Row([
                                        html.P("Here are some recommended fields based on your current skills:"),
                                    ]),
                                    dbc.Row([
                                        dbc.Row([
                                            dbc.Col(html.H4("Healthcare")),
                                            dbc.Col(dbc.Button("View Skills", size="sm")),
                                        ], justify="between"),
                                        dbc.Row([
                                            dbc.Col(html.H4("Education")),
                                            dbc.Col(dbc.Button("View Skills", size="sm")),
                                        ], justify="between"),
                                        dbc.Row([
                                            dbc.Col(html.H4("Human Resources")),
                                            dbc.Col(dbc.Button("View Skills", size="sm")),
                                        ], justify="between"),
                                        dbc.Row([
                                            dbc.Col(html.H4("Sport and Fitness")),
                                            dbc.Col(dbc.Button("View Skills", size="sm")),
                                        ], justify="between"),                 
                                    ])
                                ], width=6),
                                dbc.Col([
                                    dbc.Row([
                                        html.P("Here are some recommended jobs based on your current skills:"),
                                    ]),
                                    dbc.Row([
                                        dbc.Row([
                                            dbc.Col(html.H4("Nurse")),
                                            dbc.Col(dbc.Button("View Skills", size="sm")),
                                        ], justify="between"),
                                        dbc.Row([
                                            dbc.Col(html.H4("Teacher")),
                                            dbc.Col(dbc.Button("View Skills", size="sm")),
                                        ], justify="between"),
                                        dbc.Row([
                                            dbc.Col(html.H4("Corporate Trainer")),
                                            dbc.Col(dbc.Button("View Skills", size="sm")),
                                        ], justify="between"),
                                        dbc.Row([
                                            dbc.Col(html.H4("Sport Coach")),
                                            dbc.Col(dbc.Button("View Skills", size="sm")),
                                        ], justify="between"),                 
                                    ])
                                ], width=6),
                                ])
                            ]
                        ),         
                    ]   
                )
            ]
        )
    ]
)
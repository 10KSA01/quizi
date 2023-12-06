from dash import Dash, html, dcc, register_page
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import json
import random
import platform

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
fig.update_traces(showlegend=True)

register_page(__name__)

def create_quiz_list(title):
    return dbc.Card(
        style={
            "marginBottom": "1vh",
        },
        children=[
            dbc.CardHeader(title.title(), style={"fontSize": "1.2em"}),
            dbc.CardBody(
                children=[

                    dbc.ListGroup(
                        flush=True,
                        style={
                            "minWidth": "10vw",
                        },
                        children=[
                            create_quiz_list_item("Python", "medium"),
                            create_quiz_list_item("Python", "easy"),
                            create_quiz_list_item("Python", "hard"),
                            create_quiz_list_item("Python", "medium"),
                            create_quiz_list_item("Python", "easy"),
                            create_quiz_list_item("Python", "hard"),
                            create_quiz_list_item("Python", "medium"),
                            create_quiz_list_item("Python", "easy"),
                            create_quiz_list_item("Python", "hard"),
                            create_quiz_list_item("Python", "medium"),
                            create_quiz_list_item("Python", "easy"),
                            create_quiz_list_item("Python", "hard"),
                        ]
                    )

                ]
            )
        ]
    )

def create_quiz_list_item(title, difficulty):
    
    if difficulty == "easy":
        color = "green"
    elif difficulty == "medium":
        color = "orange"
    elif difficulty == "hard":
        color = "red"

    return dbc.ListGroupItem(
        style={
            "display": "flex",
            "justify-content": "space-between",
            "align-items": "center",
        },
        children=[

            html.Span(title.title()),
            html.Span(difficulty.title(), style={"color": color}),

        ],
        href="#"
    )

def create_quiz_card(title, subject, difficulty):
    if subject == "math": 
        src = "/assets/images/math.jpg"
    elif subject == "chemistry":
        src = "/assets/images/chemistry.jpg"
    elif subject == "science":
        src = "/assets/images/science.jpg"

    if difficulty == "easy":
        color = "green"
    elif difficulty == "medium":
        color = "orange"
    elif difficulty == "hard":
        color = "red"

    return dbc.Card(style={"margin": "1vh 1vw 0 0 ", "maxWidth": "15vw"}, children=[
                            
        dbc.CardHeader(style={"display": "flex", "justify-content": "space-between"}, children=[title.title(), html.Span(difficulty.title(), style={"color": color})]),
        
        dbc.CardBody(style={"display": "flex", "justify-content": "center", "align-items": "center"}, children=[
        
            html.Img(src=src, style={"width": "50%"}),
                                    
        ]),

        dbc.CardFooter(
            dbc.Button("Take Quiz", color="primary", style={"width": "100%"}, href="/quizstart")
        )

    ])

layout = html.Div(
    [
        # Recommended Quizzes
        html.Div(
        
            dbc.Card([
        
                dbc.CardHeader("Recommended Quizzes", style={"fontSize": "2em"}),
                
                dbc.CardBody([
                
                    # Scrollable list of recommended quizzes
                    html.Div(
                        style={
                            "display": "flex", 
                            "flex-direction": "row", 
                            "overflowX": "scroll",
                            "flex-wrap": "wrap",
                        }, 
                        children=[
                            create_quiz_card("Algebra", "math", "easy"),
                            create_quiz_card("Hydrocarbons", "chemistry", "hard"),
                            create_quiz_card("Core Science", "science", "medium"),
                            create_quiz_card("Elements", "chemistry", "easy"),
                            create_quiz_card("Calculus", "math", "medium"),
                            create_quiz_card("Oil", "chemistry", "medium"),
                        ]
                    ),
                
                    # Radar graph of user vs dream job
                    html.Div(
                        style={
                            "height": "auto", 
                            "maxHeight": "25vh",
                            "display": "flex", 
                            "justify-content": "center",
                            "align-items": "center",
                        }, 
                        children=[
                            dcc.Graph(
                                figure=fig,
                                style={"height": "100%"}
                            )
                        ]
                    )
                ],
                # dbc.CardBody containing recommended quizzes and radar graph
                style={
                    "display": "flex",
                    "justify-content": "space-between",
                    "align-items": "center",
                })
            ])
        ),

        dbc.Card(
            style={
                "marginTop": "1vh"
            },
            children=[
                dbc.CardHeader(
                    children=[
                        html.P("Quizzes by Skill", style={"fontSize": "2em"}),
                    ]
                ),
                dbc.CardBody(
                    children=[
                        html.Div(
                            style={
                                "display": "flex",
                                "flex-direction": "row",
                                "flex-wrap": "wrap",
                                "justify-content": "space-between",
                                "marginTop": "1vh",

                            },
                            children=[
                                create_quiz_list("languages"),
                                create_quiz_list("business and economics"),
                                create_quiz_list("religious and ethical studies"),
                                create_quiz_list("technology"),
                                create_quiz_list("creative arts"),
                                create_quiz_list("social studies"),
                                create_quiz_list("mathematics and sciences"),
                            ]
                        ),
                    ]
                )
            ]
        ),
    ],
    style={
        "width": "100vw", 
        "padding": "1vh 1vw"
    }
)


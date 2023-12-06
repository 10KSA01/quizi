from dash import Dash, html, dcc, register_page
import dash_bootstrap_components as dbc
import json
import platform

file_path = ""
if platform.system() == 'Windows':
    file_path = "app\\data\\baseline_quiz.json"
else:
    file_path = "data/baseline_quiz.json"
    
with open(file_path) as f:
    quiz_json_data = json.load(f)

register_page(__name__)

def create_quiz_elements(quiz_data):
    quiz_elements = []
    for question in quiz_data:
        quiz_elements.append(
            dbc.Table([
                html.Tbody(
                    html.Tr([
                        html.Td(
                            html.Th(question['question']) 
                        ),
                        html.Td(
                            html.Select(
                                [
                                    html.Option(option, value=option) for option in question['options']
                                ],
                                style={"width": "100%"}
                            )
                        )
                    ])
                )
            ], style={"width": "40%", "margin": "2vh 2vw"}, bordered=True),
        )

    quiz_elements.append(
            html.A(dbc.Button("Submit", color="success", style={"width": "100%"}), href="/ftui/ftui-3", style={"width": "100%", "margin": "2vh 2vw"})
    )

    return quiz_elements

layout = html.Div(
    create_quiz_elements(quiz_json_data),
    style={"display": "flex", "flex-wrap": "wrap", "justify-content": "center", "align-items": "center", "flex-direction": "row", "marginTop": "2vh"}
)
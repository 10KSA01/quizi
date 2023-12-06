import dash
from dash import Dash, html, dcc, register_page, dash_table
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from components.Items import example_daily_item
import math
import platform
import json
import pandas as pd


if platform.system() == 'Windows':
    score_file_path = "app/temp/cur_quiz_score.tmp"
    answer_file_path = "app/temp/cur_quiz_answered.tmp"
    quiz_json_filename_path = "app/temp/cur_quiz_json.tmp"
    data_path = "app/data"
    current_performance_path = "app/temp/cur_quiz_performance.tmp"
else:
    score_file_path = "temp/cur_quiz_score.tmp"
    answer_file_path = "temp/cur_quiz_answered.tmp"
    quiz_json_filename_path = "temp/cur_quiz_json.tmp"
    data_path = "data"
    current_performance_path = "temp/cur_quiz_performance.tmp"



register_page(__name__)



stars = 3
stars_unicode = "".join(["★"] * stars + ["☆"] * (3-stars))

with open(score_file_path, "r") as f_r:
    correct = int(float(f_r.read()))
with open(answer_file_path, "r") as f_r:
    answered = int(float(f_r.read()))

def create_scoreboard_list(type):
    if type == "friends":
        friend_names = ["bob", "dave", "steve", "mary"]
    else:
        friend_names = ["", "", "", ""]

    return dbc.ListGroup(
        style={},
        children=[
            create_scoreboard_list_item(
                1,
                friend_names[0],
                80,
                "10:34"
            ),
            create_scoreboard_list_item(
                2,
                friend_names[1],
                80,
                "12:34"
            ),
            create_scoreboard_list_item(
                3,
                friend_names[2],
                40,
                "6:34"
            ),
            create_scoreboard_list_item(
                4,
                friend_names[3],
                8,
                "1:34"
            ),
        ]
    )

def create_scoreboard_list_item(ranking, friend_name, score_percentage, time):
    return dbc.ListGroupItem(
        style={
            "display": "flex",
            "justify-content": "space-between",
        },
        children=[
            html.Span(str(ranking)),
            html.Span(friend_name),
            dbc.Progress(label=str(score_percentage) + "%", value=score_percentage, style={"width": "50%"}),
            html.Span(time),
        ]
    )

layout = html.Div(
    style={
        "padding": "2vh 2vw"
    },
    children=[

        # Top row with quiz name and next button
        html.Div(
            style={
                "display": "flex",
                "justify-content": "space-between",
            },
            children=[
                html.H3("Quiz Name"),
                dbc.Button(
                    style={"textAlign": "left"},
                    children=[
                        html.Span("Next Quiz", style={"fontSize": "1.2em"}),
                        html.Br(),
                        html.Span("Algebra"),
                    ],
                    color="primary",
                    href="/quizstart"
                ),
            ]
        ),

        # Progress bar row
        html.Div(
            style={
                "display": "flex",
                "justify-content": "space-around",
                "padding": "10vh 0"
            },
            children=[
                html.H2("9"),
                dbc.Progress(
                    [
                        dbc.Progress(value=0, color="primary", bar=True, id="xp-bar-base"),
                        dbc.Progress(value=10, color="success", bar=True, id="xp-bar-growth", label="+27 XP", striped=True, animated=True),
                    ],
                    style={
                        "width": "90%",
                        "height": "5vh"
                    }
                ),
                dcc.Interval(
                    id="xp-bar-timer",
                    interval=100,  # Update every millisecond
                    n_intervals=0,
                    disabled=False
                ),
                html.H2("10")
            ]
        ),

        # Reward row
        html.Div(
            style={
                "padding": "5vh 0 ",
            },
            children=[
                dbc.Row(
                    style={
                        "flex-wrap": "nowrap",
                        "display": "flex",
                        "justify-content": "center"
                    },
                    children=[
                        dbc.Col([example_daily_item("Title", "Algebra Admiral", check=False)], width={"size": 2}),
                        dbc.Col([example_daily_item("Points", "+15 points", check=False)], width={"size": 2}),
                    ],
                    className="overflow-auto",
                ),
            ]
        ),

        # div to contain breakdown and friends score
        html.Div(
            style={
                "display": "flex",
                "width": "100%",
                "justify-content": "space-evenly",
                "flex-direction": "row",
            },

            children=[

            # Score breakdown row
            html.Div(
                style={
                    "width": "45vw",
                    #"border": "solid black 1px"
                },
                children=[
                    html.Div(children=[
                        html.H3("Score: 3/5 (--%)",
                                id="quizscore"),
                        html.H3("Quiz breakdown"),
                        html.Div([],
                            id="quiz-breakdown-div"
                        ),
                    ])
                ]
            ),

            # Scoreboard
            html.Div(
                style={
                    "width": "45vw"
                },
                children=[
                    dbc.Card(
                        style={},
                        children=[
                            dbc.Tabs(
                                style={},
                                children=[
                                    dbc.Tab(
                                        label="Your Scores",
                                        tab_id="tab-1",
                                        children=[
                                            html.Div(
                                                style={},
                                                children=[
                                                    create_scoreboard_list(None)
                                                ]
                                            ),
                                        ]
                                    ),
                                    dbc.Tab(
                                        label="Friends",
                                        tab_id="tab-2",
                                        children=[
                                            html.Div(
                                                style={},
                                                children=[
                                                    create_scoreboard_list("friends")
                                                ]
                                            ),
                                        ]
                                    ),
                                    dbc.Tab(
                                        label="Global",
                                        tab_id="tab-3",
                                        children=[
                                            html.Div(
                                                style={},
                                                children=[
                                                    create_scoreboard_list("friends")
                                                ]
                                            ),
                                        ]
                                    ),
                                ],
                            )
                        ]
                    )
                ]
            ),

        ])



    ]
)

# layout = dbc.Container([
#     # First Row
#     dbc.Row([
#         dbc.Col(
#             dbc.Card([
#                 html.H3("Quiz title"),
#             ]),
#             width=6  # This column takes half of the row
#         ),
#         dbc.Col(
#             dbc.Card([
#                 html.H3(f"Difficulty: {stars_unicode}"),
#             ]),
#             width=4
#         ),

#         dbc.Col(
#             dbc.Card([
#                 dbc.Button([
#                     html.H3("Next Quiz")
#                 ], color="primary", style={"width": "100%"}, href="/quizstart"),
#             ]),
#             width=2 # last 2/12ths of a row
#         ),
#     ],
#         className="m-2",
#     ),

#     # level up bar row
#     dbc.Row([
#         dbc.Col([
#             dbc.Card([
#                 html.H2("Level 9"),
#                 dbc.Progress(
#                     [
#                         dbc.Progress(value=0, color="warning", bar=True, id="xp-bar-base"),
#                         dbc.Progress(value=10, color="success", bar=True, id="xp-bar-growth"),
#                     ]
#                 ),
#                 dcc.Interval(
#                     id="xp-bar-timer",
#                     interval=100,  # Update every millisecond
#                     n_intervals=0,
#                     disabled=False
#                 )
#             ])

#         ], width=9),

#         dbc.Col([
#             dbc.Card([
#                 html.H2("+27 XP")
#             ])
#         ], width=3),
#     ],
#         className="m-2",
#     ),

#     dbc.Row([
#         dbc.Col([

#             dbc.Row([
#                 dbc.Card([
#                     html.H3(f"Score: {correct}/{answered} ({((correct * 100) // answered) if answered != 0 else '--'}%)",
#                             id="quizscore")
#                 ]),
#             ]),

#             dbc.Row([

#                 dbc.Card([
#                     html.H3("Quiz breakdown"),
#                     html.P("Maybe by question")
#                 ]),
#             ]),

#         ],
#             width=6,
#         ),

#         # Second Column in the second row
#         dbc.Col([
#             dbc.Row([

#                 dbc.Card([
#                     html.H3("Friend scoreboard"),
#                 ]),
#             ]),
#         ],
#             width=6
#         ),
#     ],
#         className="m-3"
#     ),
# ])


@dash.callback(
    [
        Output("xp-bar-base", "value"),
        Output("xp-bar-growth", "value"),
        Output("xp-bar-timer", "disabled"),
    ],
    [
        Input("xp-bar-timer", "n_intervals"),
    ]
)
def xp_bar_growth(timer_count):

    # all arbitrary (and static)
    xp_pre_quiz = 35
    xp_gain = 20
    slow_rate = 500 # damper
    offset = 8

    shown = xp_gain
    shown *= (offset * math.log(((timer_count / slow_rate) + 0.1), 10) + offset)

    #print(shown)

    if shown > xp_gain:
        return [xp_pre_quiz, xp_gain, True]

    return [
        xp_pre_quiz, min(xp_gain, shown), False
    ]
    
@dash.callback(
    Output("quizscore", "children"),
    [
        Input("xp-bar-timer", "n_intervals"),
        Input("quizscore", "children"),

    ]
)
def update_score(timer_count, old):
    global correct
    global answered

    with open(score_file_path, "r") as f_r:
        correct = int(f_r.read())
    with open(answer_file_path, "r") as f_r:
        answered = int(f_r.read())

    if answered == 0:
        with open(score_file_path, "r") as f_w:
            f_w.write(f"0")
        with open(answer_file_path, "r") as f_w:
            f_w.write(f"0")

        return old

    return f"Score: {correct}/{answered} ({((correct * 100) // answered) if answered != 0 else '--'}%)"



@dash.callback(
    Output("quiz-breakdown-div", "children"),
    Input("xp-bar-timer", "n_intervals")
)
def update_quiz_breakdown(timer_count):

    # read question data from json
    with open(quiz_json_filename_path, "r") as f_r:
        with open(f"{data_path}/{f_r.read().strip()}", "r") as json_r:
            try:
                raw = json.loads(json_r.read().strip())
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")

    with open(current_performance_path, "r") as f_r:
        pairs = f_r.read().split("\n")

    if pairs == ['']:
        return html.P("No data found. Try completing a quiz!")

    #print(pairs)

    qs = [q["question"] for q in raw]
    gs = [g.split()[0] for g in pairs if g != '']
    cs = [g.split()[1] for g in pairs if g != '']

    data = {
        "Question": qs,
        "Correct": cs,
        "Given": gs
    }

    #print(data)

    df = pd.DataFrame(data)

    return [dash_table.DataTable(
        id="quiz-breakdown",
        columns=[
            {"name": "Question", "id": "Question"},
            {"name": "Correct answer", "id": "Correct"},
            {"name": "Your answer", "id": "Given"},
        ],
        data=df.to_dict('records'),
        style_table={'height': '450px'},
        style_cell={'textAlign': 'left'},
        style_data={
            'whiteSpace': 'normal',
            'height': 'auto',
            'lineHeight': '15px'
        },
    )]

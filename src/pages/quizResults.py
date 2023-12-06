import dash
from dash import Dash, html, dcc, register_page
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import math
import platform


if platform.system() == 'Windows':
    score_file_path = "app/temp/cur_quiz_score.tmp"
    answer_file_path = "app/temp/cur_quiz_answered.tmp"
else:
    score_file_path = "temp/cur_quiz_score.tmp"
    answer_file_path = "temp/cur_quiz_answered.tmp"



register_page(__name__)



stars = 3
stars_unicode = "".join(["★"] * stars + ["☆"] * (3-stars))

with open(score_file_path, "r") as f_r:
    correct = int(f_r.read())
with open(answer_file_path, "r") as f_r:
    answered = int(f_r.read())


# Use the Dash app with a Bootstrap theme

layout = dbc.Container([
    # First Row
    dbc.Row([
        dbc.Col(
            dbc.Card([
                html.H3("Quiz title"),
            ]),
            width=6  # This column takes half of the row
        ),
        dbc.Col(
            dbc.Card([
                html.H3(f"Difficulty: {stars_unicode}"),
            ]),
            width=4
        ),

        dbc.Col(
            dbc.Card([
                dbc.Button([
                    html.H3("Next Quiz")
                ], color="primary", style={"width": "100%"}, href="/quizstart"),
            ]),
            width=2 # last 2/12ths of a row
        ),
    ],
        className="m-2",
    ),

    # level up bar row
    dbc.Row([
        dbc.Col([
            dbc.Card([
                html.H2("Level 9"),
                dbc.Progress(
                    [
                        dbc.Progress(value=0, color="warning", bar=True, id="xp-bar-base"),
                        dbc.Progress(value=10, color="success", bar=True, id="xp-bar-growth"),
                    ]
                ),
                dcc.Interval(
                    id="xp-bar-timer",
                    interval=100,  # Update every millisecond
                    n_intervals=0,
                    disabled=False
                )
            ])

        ], width=9),

        dbc.Col([
            dbc.Card([
                html.H2("+27 XP")
            ])
        ], width=3),
    ],
        className="m-2",
    ),

    dbc.Row([
        dbc.Col([

            dbc.Row([
                dbc.Card([
                    html.H3(f"Score: {correct}/{answered} ({((correct * 100) // answered) if answered != 0 else '--'}%)",
                            id="quizscore")
                ]),
            ]),

            dbc.Row([

                dbc.Card([
                    html.H3("Quiz breakdown"),
                    html.P("Maybe by question")
                ]),
            ]),

        ],
            width=6,
        ),

        # Second Column in the second row
        dbc.Col([
            dbc.Row([

                dbc.Card([
                    html.H3("Friend scoreboard"),
                ]),
            ]),
        ],
            width=6
        ),
    ],
        className="m-3"
    ),
])


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

    print(shown)

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


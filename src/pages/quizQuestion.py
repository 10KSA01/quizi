# page to be used during a quiz
import dash
from dash import Dash, html, dcc, register_page
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import platform
import json

register_page(__name__)


###############
# setup files #
###############

score_file_path = ""
answer_file_path = ""

if platform.system() == 'Windows':
    score_file_path = "app/temp/cur_quiz_score.tmp"
    answer_file_path = "app/temp/cur_quiz_answered.tmp"
    quiz_json_filename_path = "app/temp/cur_quiz_json.tmp"
    data_path = "app/data"
else:
    score_file_path = "temp/cur_quiz_score.tmp"
    answer_file_path = "temp/cur_quiz_answered.tmp"
    quiz_json_filename_path = "temp/cur_quiz_json.tmp"
    data_path = "data"


with open(score_file_path, "w") as f_w:
    f_w.write("0")
with open(answer_file_path, "w") as f_w:
    f_w.write("0")
with open(quiz_json_filename_path, "w") as f_w:
    f_w.write("baseline_quiz.json")


with open(quiz_json_filename_path, "r") as f_r:
    with open(f"{data_path}/{f_r.read().strip()}", "r") as json_r:
        try:
            raw = json.loads(json_r.read().strip())
            questionSet = [raw[n]["question"] for n in range(len(raw))]
            answerSet = [raw[n]["options"] for n in range(len(raw))]
            correctSet = [raw[n]["answer"] for n in range(len(raw))]
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")


c_answers = 0

#answers = ["Went", "Goed", "Gone", "Going"]
#correct = "A"
q_completed = 0
q_questions = len(questionSet)

stars = 3
stars_unicode = "".join(["★"] * stars + ["☆"] * (3-stars))

# only runs on page load
# so can use answerSet[0]
buttons = [
        dbc.Row([
            dbc.Card([
                html.Div([
                    html.H3(f"{answer}",
                            id=f"quizbutton-{n+1}-text"),
                ],
                    id=f"quizbutton-{n+1}"
                ),

            ])
        ])
        for n, answer in enumerate(answerSet[0])
    ]

# layout = dbc.CardBody([
#     html.Br(),
#     dbc.Row([
#         dbc.Col(html.H1("Quiz title"), width={"offset": 1}),
#         dbc.Col(dbc.Button("Start", href="/quizquestion"),width={"offset": 6})
#     ]),
    
# ])
layout = dbc.Container([
    # First Row
    dbc.Row([
        # First Column in the first row
        dbc.Col(
            dbc.Card([
                html.H3("Quiz title"),
            ]),
            width=6  # This column takes half of the row
        ),

        # Second Column in the first row
        dbc.Col(
            dbc.Card([
                html.H3(f"Difficulty: {stars_unicode}"),
            ]),
            width=4
        ),

        dbc.Col(
            dbc.Card([
                html.H3(f"Q: {q_completed + 1} / {q_questions}",
                        id="quizfraction"),
            ]),
            width=2 # last 2/12ths of a row
        ),
    ],
        className="m-2",
    ),

    dbc.Row([
        dbc.Card([
            html.H4("timer progress bar if possible"),
        ])
    ],
        className="m-2",
    ),

    dbc.Row([

        dbc.Card([
            #html.H1(f"{questionSet[pointer]}",
            html.H1(f"Question loading",
                    id="quizquestion"),
            html.H3("Here is some question context or description")

        ])
    ],
        className="m-2",
    ),


    dbc.Row([
        # First Column in the second row
        dbc.Col([
            buttons[0],
            buttons[2]
        ],
            width=6,
        ),

        dbc.Col([

            buttons[1],
            buttons[3]

        ],
            width=6,
        ),


    ]),

    dcc.Location(id='url'),
])


@dash.callback(
    [
        Output("quizbutton-1", "n_clicks_timestamp"),
        Output("quizbutton-2", "n_clicks_timestamp"),
        Output("quizbutton-3", "n_clicks_timestamp"),
        Output("quizbutton-4", "n_clicks_timestamp"),
        #Output("url", "pathname"),
        Output("quizquestion", "children"),
        Output("quizfraction", "children"),
        Output("quizbutton-1-text", "children"),
        Output("quizbutton-2-text", "children"),
        Output("quizbutton-3-text", "children"),
        Output("quizbutton-4-text", "children"),
        Output("url", "pathname"),
    ],
    [
        Input("quizbutton-1", "n_clicks_timestamp"),
        Input("quizbutton-2", "n_clicks_timestamp"),
        Input("quizbutton-3", "n_clicks_timestamp"),
        Input("quizbutton-4", "n_clicks_timestamp"),
    ],
)
def add_score_callback(b1, b2, b3, b4):
    # defaults to -1, max is most recent

    global q_completed
    global q_questions

    #with open(score_file_path, "r") as f_r:
    #    q_completed = int(f_r.read())
    #with open(answer_file_path, "r") as f_r:
    #    q_questions = int(f_r.read())

    # would read length of json array every time
    # however, for demo, we set to 10 and pray
    q_questions = len(questionSet)


    bs = [(n if n is not None else -1) for n in [b1, b2, b3, b4]]
    m = max(bs)
    mInd = max(enumerate(bs), key=lambda x: x[1])[0]
    #print(bs, m, mInd)

    # sometimes callbacks just happen, not sure why. This prevents them being processed
    if m > -1:
        #print("ABCD"[mInd])
        if "ABCD"[mInd] == correctSet[q_completed]:
            with open(score_file_path, "r") as f_r:
                cur_score = int(f_r.read())
            with open(score_file_path, "w") as f_w:
                f_w.write(f"{cur_score + 1}")

        with open(answer_file_path, "r") as f_r:
            cur_score = int(f_r.read())
        with open(answer_file_path, "w") as f_w:
            f_w.write(f"{cur_score + 1}")


        q_completed += 1


        if q_completed == q_questions:
            print("STOPSTOPSTOP")

            q_completed = 0

            return [None] * 10 + ["/quizresults"]

        #TODO: change to new page

    # Reset button click times
    return [-1] * 4 + [questionSet[q_completed], f"Q {q_completed+1}/{q_questions}"] + answerSet[q_completed] + [None]




from dash import Dash, dcc, html, dash_table
import dash_bootstrap_components as dbc
import pandas as pd

# Sample data for DataTables
# recent_quest = {'': ['Completed Quest: Addition Level 3 (7/10)', 'Completed Quest: Subtraction Level 2 (8/10)', 'Completed Quest: Addition Level 1 (10/10)']}
recent_quest = {'Quest': ['Algebra Level 2', 'Calculus Level 3', 'Addition Level 1'], 'Difficulty': ['Hard', 'Hard', 'Easy'], 'Score': ['14/20 in 166 seconds', '4/10 in 214 seconds', '10/10 in 60 seconds']}
friend_quest = {'Friend':['John', 'Alice', 'Bob'], 'Quest': ['Algebra Level 2', 'Calculus Level 3', 'Addition Level 1'], 'Difficulty': ['Hard', 'Hard', 'Easy'], 'Score': ['14/20 in 166 seconds', '4/10 in 214 seconds', '10/10 in 60 seconds']}
daily_quest = {'': ['New Quest: Addition Level 4', 'New Quest: Subtraction Level 3', 'New Quest: Multiplication Level 1']}
your_score = {
    '': [
        '3/3 in 60 secs', 
        '3/3 in 80 secs', 
        '3/3 in 90 secs', 
        '3/3 in 110 secs', 
        '3/3 in 120 secs', 
        '2/3 in 70 secs', 
        '2/3 in 80 secs', 
        '2/3 in 95 secs'
    ]
}
friend_score = {'': ['John Score: 3/3, Date: 05/12/2023, Time: 70 seconds', 'Alice Score: 3/3, Date: 05/12/2023, Time: 82 seconds', 'Bob Score: 3/3, Date: 04/12/2023, Time: 98 seconds', 'Bob Score: 3/3, Date: 03/12/2023, Time: 113 seconds', 'Alice Score: 3/3, Date: 02/12/2023, Time: 120 seconds', 'John Score: 2/3, Date: 01/12/2023, Time: 71 seconds', 'Alice Score: 2/3, Date: 30/11/2023, Time: 82 seconds', 'John Score: 2/3, Date: 25/11/2023, Time: 98 seconds']}
global_score = {'Rank': ['Rank: 1', 'Rank: 2', 'Rank: 3', 'Rank: 4', 'Rank: 5', 'Rank: 6', 'Rank: 7', 'Rank: 8'], 'Name':['Sheldon', 'Ali', 'Bob', 'May', 'Amy', 'Johny', 'Jack', 'Leo'], 'Time':['10 seconds', '11 seconds', '12 seconds', '13 seconds', '14 seconds', '15 seconds', '16 seconds', '17 seconds']}


df_recent_quest = pd.DataFrame(recent_quest)
df_friend_quest = pd.DataFrame(friend_quest)
df_daily_quest = pd.DataFrame(daily_quest)
df_your_score = pd.DataFrame(your_score)
df_friend_score = pd.DataFrame(friend_score)
df_global_score = pd.DataFrame(global_score)

def example_activity_friends():
    activity_table = html.Div(
        [
            dbc.Card([
                dbc.Tabs([
                    dbc.Tab(label='Recent Activity', children=[
                        html.Div([
                            dash_table.DataTable(
                                id='table-1',
                                columns=[{'name': col, 'id': col} for col in df_recent_quest.columns],
                                data=df_recent_quest.to_dict('records'),
                                style_table={'height': '450px'},
                                style_cell={'textAlign': 'left'}
                            ),
                        ]),
                    ]),
                    dbc.Tab(label='Friends Activity', children=[
                        html.Div([
                            dash_table.DataTable(
                                id='table-2',
                                columns=[{'name': col, 'id': col} for col in df_friend_quest.columns],
                                data=df_friend_quest.to_dict('records'),
                                style_table={'height': '450px'},
                                style_cell={'textAlign': 'left'}
                            ),
                        ]),
                    ]),
                ]),
            ]),
        ]
    )
    
    return activity_table

def example_quest_score():
    activity_table = html.Div(
        [
            dbc.Card([
                dbc.Tabs([
                    dbc.Tab(label='Your Score', children=[
                        html.Div([
                            dash_table.DataTable(
                                id='table-4',
                                columns=[{'name': col, 'id': col} for col in df_your_score.columns],
                                data=df_your_score.to_dict('records'),
                                style_table={'height': '410px', 'marginTop': "-3.5vh"},
                                style_cell={'textAlign': 'center'},
                                style_header={'display': 'none'}

                            ),
                        ]),
                    ]),
                    dbc.Tab(label='Friend Score', children=[
                        html.Div([
                            dash_table.DataTable(
                                id='table-5',
                                columns=[{'name': col, 'id': col} for col in df_friend_score.columns],
                                data=df_friend_score.to_dict('records'),
                                style_table={'height': '410px'},
                                style_cell={'textAlign': 'left'}
                            ),
                        ]),
                    ]),
                    dbc.Tab(label='Global Score', children=[
                        html.Div([
                            dash_table.DataTable(
                                id='table-6',
                                columns=[{'name': col, 'id': col} for col in df_global_score.columns],
                                data=df_global_score.to_dict('records'),
                                style_table={'height': '410px'},
                                style_cell={'textAlign': 'left'}
                            ),
                        ]),
                    ]),
                ]),
            ],className="border-0 bg-transparent",
            ),
        ]
    )
    
    return activity_table

def example_daily_quest():
    daily_table = html.Div(
        [
            dbc.Card([
                dbc.CardHeader("Daily Quest"),
                dash_table.DataTable(
                    id='table-3',
                    columns=[{'name': col, 'id': col} for col in df_daily_quest.columns],
                    data=df_daily_quest.to_dict('records'),
                    style_cell={'textAlign': 'left'}
                ),
            ])
        ]
    )
    
    return daily_table
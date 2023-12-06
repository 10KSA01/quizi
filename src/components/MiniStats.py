import dash_bootstrap_components as dbc
from dash import html


card_icon = {
    "textAlign": "center",
    "fontSize": "1em",
    "margin": "auto",
}
def mini_stat(icon, text):
    card = dbc.Card(
        [
            dbc.Row([
                html.Div(className=icon, style=card_icon)
            ]),
            dbc.Row(html.H4(text)),
        ],
        className="border-0 bg-transparent",
        style={"width": "5rem", "text-align": "center"},
    )
    return card
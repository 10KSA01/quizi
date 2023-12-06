from dash import Dash, html, page_container
import dash_bootstrap_components as dbc
from components.navbar import create_navbar

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP], use_pages=True)

app.title = 'Quizi'
app._favicon = ('logo.ico')
navbar = create_navbar()

server = app.server

app.layout = html.Div(
    [
        dbc.Row(
            [
                navbar,
                html.Div(page_container),
            ],
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True, port=8075)
from dash import Dash, html, dcc, register_page
import dash_bootstrap_components as dbc
from components.Items import example_shop_item


register_page(__name__)

layout = dbc.CardBody(
    [
        html.Br(),
        dbc.Row([
            dbc.Col(
                [
                    html.H2("Welcome to the Shop"),
                    html.P("Explore our collection of accessories and make your purchase."),
                ],
                width=12, className="text-center"
            ),
        ]),
        html.Br(),
        dbc.Row(dbc.Col(html.H2("Accessories"), width={"offset": 1})),
        dbc.Row(
            [
                dbc.Col([example_shop_item("Border 1", "15 points", "/assets/images/borders/border1.jpg")], width={"offset": 1, "size": 2}),
                dbc.Col([example_shop_item("Border 2", "20 points", "/assets/images/borders/border2.jpg")], width=2),
                dbc.Col([example_shop_item("Border 3", "50 points", "/assets/images/borders/border3.jpg")], width=2),
                dbc.Col([example_shop_item("Border 4", "150 points", "/assets/images/borders/border4.jpg")], width=2),
                dbc.Col([example_shop_item("Border 5", "200 points", "/assets/images/borders/border5.jpg")], width=2),
                dbc.Col([example_shop_item("Title 1", "100 points", "/assets/images/Titles/title1.png")], width=2),
                dbc.Col([example_shop_item("Title 2", "100 points", "/assets/images/Titles/title2.png")], width=2),
                dbc.Col([example_shop_item("Title 3", "100 points", "/assets/images/Titles/title3.png")], width=2),
                dbc.Col([example_shop_item("Background 1", "200 points", "/assets/images/Background/bg1.jpg")], width=2),
                dbc.Col([example_shop_item("Background 2", "200 points", "/assets/images/Background/bg2.jpg")], width=2),
                dbc.Col([example_shop_item("Background 3", "200 points", "/assets/images/Background/bg3.jpg")], width=2),
                dbc.Col("", width={"offset": 1}),
            ],
            className="overflow-auto",
            style={"flex-wrap": "nowrap"}
                
        ),
        html.Br(),
        dbc.Row(dbc.Col(html.H2("Points"), width={"offset": 1})),
        dbc.Row(
            [
                dbc.Col([example_shop_item("10 points","$1", "/assets/images/Money/money10.jpg")], width=2),
                dbc.Col([example_shop_item("50 points","$4", "/assets/images/Money/money50.jpg")], width=2),
                dbc.Col([example_shop_item("100 points","$7", "/assets/images/Money/money100.jpg")], width=2),
                dbc.Col([example_shop_item("500 points", "$40", "/assets/images/Money/money500.jpg")], width=2),
            ],
            align="center",
            justify="center"
        ),
        html.Br()
    ]
)
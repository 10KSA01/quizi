from dash import html, dcc
import dash_bootstrap_components as dbc

logo = "/assets/images/logo.png"
def create_navbar():
    logo_element = [
        dbc.Row([
            dbc.Col(html.Img(src=logo, height="30vh")),
            dbc.Col(dbc.NavbarBrand("Quizi")),
    ])]
    return dbc.NavbarSimple(
        style={
            "padding": "0.5vh 2vw",
            "height": "10vh",
            "lineHeight": "5vh",
            "fontSize": "1.2em"
        },
        children=[
            dbc.NavItem(dbc.NavLink("Home", href="/", style={"marginTop": "1.5vh"})),
            dbc.NavItem(dbc.NavLink("Shop", href="/shop", style={"marginTop": "1.5vh"})),
            dbc.NavItem(dbc.NavLink("Quiz", href="/quizselection", style={"marginTop": "1.5vh"})),
            dbc.DropdownMenu(
                style={"marginTop": "1.5vh"},
                children=[
                    dbc.DropdownMenuItem("Profile", href="#"),
                    dbc.DropdownMenuItem("Settings", href="#"),
                ],
                nav=True,
                in_navbar=True,
                label="Profile",
            ),
            dbc.NavItem(dbc.NavLink("Level 66", style={"marginTop": "1.5vh"})),
            dbc.NavItem(dbc.NavLink(className="bi bi-coin"), style={"marginRight": "-0.2vw", "marginTop": "1.5vh"}),
            dbc.NavItem([dbc.NavLink("455")], style={"marginTop": "1.5vh"}),
            dbc.NavItem(
                style={
                    "marginLeft": "1vw"
                },
                children=[
                    html.Div(
                        style={
                            "display": "flex",
                            "justifyContent": "space-between",
                            "alignItems": "center",
                            "flexDirection": "column",
                        },
                        children=[
                            html.Img(src="/assets/images/borders/border1.jpg", style={"width": "2vw", "borderRadius": "50%", "marginBottom": "-1vh"}),
                            html.Div(
                                style={
                                    "display": "flex",
                                    "justifyContent": "flex-start",
                                    "alignItems": "center",
                                    "flexDirection": "column",
                                },
                                children=[
                                    html.Span("Yusif", style={"marginBottom": "-3vh"}),
                                    html.Span("Newbie", style={"color": "#aaa", "fontSize": "0.8rem"}),
                                ]
                            )
                        ]
                    ),
                ]
            )
            
        ],
        brand=logo_element,
        brand_href="/",
        color="light",
        light=True,
        fluid=True,
    )
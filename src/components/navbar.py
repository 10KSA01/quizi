from dash import html, dcc
import dash_bootstrap_components as dbc

logo = "/assets/images/logo.png"
def create_navbar():
    logo_element = [
        dbc.Row([
            dbc.Col(html.Img(src=logo, height="30px")),
            dbc.Col(dbc.NavbarBrand("Quizi")),
    ])]
    return dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Home", href="/")),
            dbc.NavItem(dbc.NavLink("Shop", href="/shop")),
            dbc.NavItem(dbc.NavLink("Quiz", href="/quizselection")),
            dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem("Profile", href="#"),
                    dbc.DropdownMenuItem("Settings", href="#"),
                ],
                nav=True,
                in_navbar=True,
                label="Profile",
            ),
            dbc.NavItem(dbc.NavLink("Level 66")),
            dbc.NavItem(dbc.NavLink(className="bi bi-coin"), style={"marginRight": "-0.2vw"}),
            dbc.NavItem([dbc.NavLink("455")]),
            
        ],
        brand=logo_element,
        brand_href="/",
        color="light",
        light=True,
        fluid=True,
        style={"padding": "0.5vh 2vw"}
    )
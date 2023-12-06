from dash import Input, Output, State, html, callback
import dash_bootstrap_components as dbc
import platform

placeholder_path = ""
if platform.system() == 'Windows':
    placeholder_path = "/assets/images/placeholder.png"  # Note the leading '/'
else:
    placeholder_path = "/assets/images/placeholder.png"

def example_shop_item(item, cost, img):
    modal_id = f"modal_{item.replace(' ', '_').lower()}"
    card = dbc.Card(
        [
            dbc.CardImg(src=img, top=True),
            dbc.CardBody(
                [
                    html.H4(item, className="card-title"),
                    dbc.Button(str("Buy for "+ cost), id=f"open_{item.replace(' ', '_').lower()}", n_clicks=0, color="primary", className="mx-auto d-block"),
                    dbc.Modal(
                        [
                            dbc.ModalHeader(dbc.ModalTitle("Confirmation")),
                            dbc.ModalBody("Are you sure you want to buy this?"),
                            dbc.ModalFooter(
                                dbc.Button(
                                    "Pay Now", color="success", id=f"modal_close_{item.replace(' ', '_').lower()}", className="ms-auto", n_clicks=0
                                )
                            ),
                        ],
                        id=modal_id,
                        is_open=False,
                    ),
                ]
            ),
        ],
        className="d-grid mx-auto"
    )
    
    return card

items = ["Border 1", "Border 2", "Border 3", "Border 4", "Border 5", "Title 1", "Title 2", "Title 3", "Background 1", "Background 2", "Background 3", "10 points", "50 points", "100 points", "500 points", ]

@callback(
    [Output(f"modal_{item.replace(' ', '_').lower()}", "is_open") for item in items],
    [Input(f"open_{item.replace(' ', '_').lower()}", "n_clicks") for item in items],
    [Input(f"modal_close_{item.replace(' ', '_').lower()}", "n_clicks") for item in items],
    [State(f"modal_{item.replace(' ', '_').lower()}", "is_open") for item in items],
    prevent_initial_call=True
)
def toggle_modal(*args):
    n_clicks_indices = [i for i, n_clicks in enumerate(args) if n_clicks is not None]
    if n_clicks_indices:
        modal_index = n_clicks_indices[0]
        return [not is_open if i == modal_index else is_open for i, is_open in enumerate(args[-len(items):])]
    return [False] * len(items)


def example_daily_item(day, xp, check):
    card = dbc.Card(
        [
            dbc.CardHeader(day),
            dbc.CardBody(
                [
                    html.H4(xp, className="card-title"),
                    html.H4(className="bi bi-check-lg") if check else None,
                ]
            ),
        ],
        className="d-grid mx-auto"
    )
    
    return card

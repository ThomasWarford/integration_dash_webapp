# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd
import numpy as np
from solver import Solver

INITIAL_CONDITIONS = np.array([1.0, 1.0, 0])
STEP_SIZE = 0.01
TOTAL_TIME = 100
SYSTEMS = {
    "Lorenz attractor": ["10 * (y - x)", "28*x - y - x*z", "x* y - 8/3 * z"],
    "circle": ["-y", "x", "0"],
    "constant driven Brusselator (b=2.5)": [
        "1 - 3.5*x + x**2*y",
        "2.5*x - x**2*y",
        "0",
    ],
    "periodic driven Brusselator (b=2.5, omega=sqrt(2), epsilon=0.25)": [
        "1 - (2.5*(1 + 0.25*np.cos(np.sqrt(2)*t)) + 1)*x + x**2*y",
        "2.5*(1 + 0.25*np.cos(np.sqrt(2)*t))*x - x**2*y",
        "0",
    ],
}


app = Dash(__name__, external_stylesheets=[dbc.themes.LUX])

app.layout = html.Div(
    [
        html.H1("Tom's Numerical Integration Webapp", style={"textAlign": "center"}),
        html.Table(
            [
                html.Tr(
                    [
                        html.Td(
                            dcc.Graph(
                                id="solution_plot",
                                style={
                                    "height": "90vh",
                                    "width": "90vh",
                                    "textAlign": "center",
                                },
                            ),
                        ),
                        html.Td(
                            [
                                html.H3("Select Dynamical System"),
                                dcc.Dropdown(
                                    list(SYSTEMS.keys()),
                                    "Lorenz attractor",
                                    id="dyanamic_system_key",
                                ),
                                html.Br(),
                                html.Table(
                                    [
                                        html.Tr(
                                            [
                                                html.Th("Update Rules"),
                                                html.Th("Start Value"),
                                                html.Th("Total Time / s"),
                                            ]
                                        ),
                                        html.Tr(
                                            [
                                                html.Td(
                                                    [
                                                        "\u1E8B=",
                                                        dcc.Input(
                                                            id="x_update_formula",
                                                            value=SYSTEMS[
                                                                "Lorenz attractor"
                                                            ][0],
                                                            type="text",
                                                        ),
                                                    ]
                                                ),
                                                html.Td(
                                                    [
                                                        "x=",
                                                        dcc.Input(
                                                            id="x_initial",
                                                            type="number",
                                                            value=INITIAL_CONDITIONS[0],
                                                        ),
                                                    ]
                                                ),
                                                html.Td(
                                                    dcc.Input(
                                                        id="total_time",
                                                        type="number",
                                                        value=TOTAL_TIME,
                                                    )
                                                ),
                                            ]
                                        ),
                                        html.Tr(
                                            [
                                                html.Td(
                                                    [
                                                        "\u1E8F=",
                                                        dcc.Input(
                                                            id="y_update_formula",
                                                            value=SYSTEMS[
                                                                "Lorenz attractor"
                                                            ][1],
                                                            type="text",
                                                        ),
                                                    ]
                                                ),
                                                html.Td(
                                                    [
                                                        "y=",
                                                        dcc.Input(
                                                            id="y_initial",
                                                            type="number",
                                                            value=INITIAL_CONDITIONS[1],
                                                        ),
                                                    ]
                                                ),
                                                html.Th("Time Step / s"),
                                            ]
                                        ),
                                        html.Tr(
                                            [
                                                html.Td(
                                                    [
                                                        "\u017C=",
                                                        dcc.Input(
                                                            id="z_update_formula",
                                                            value=SYSTEMS[
                                                                "Lorenz attractor"
                                                            ][2],
                                                            type="text",
                                                        ),
                                                    ]
                                                ),
                                                html.Td(
                                                    [
                                                        "z=",
                                                        dcc.Input(
                                                            id="z_initial",
                                                            type="number",
                                                            value=INITIAL_CONDITIONS[2],
                                                        ),
                                                    ]
                                                ),
                                                html.Td(
                                                    dcc.Input(
                                                        id="step_size",
                                                        type="number",
                                                        value=STEP_SIZE,
                                                    )
                                                ),
                                            ]
                                        ),
                                    ]
                                ),
                            ]
                        ),
                    ]
                )
            ]
        ),
    ]
)


@app.callback(
    Output(component_id="solution_plot", component_property="figure"),
    Input(component_id="x_update_formula", component_property="value"),
    Input(component_id="y_update_formula", component_property="value"),
    Input(component_id="z_update_formula", component_property="value"),
    Input(component_id="x_initial", component_property="value"),
    Input(component_id="y_initial", component_property="value"),
    Input(component_id="z_initial", component_property="value"),
    Input(component_id="total_time", component_property="value"),
    Input(component_id="step_size", component_property="value"),
)
def update_figure(
    x_update_formula,
    y_update_formula,
    z_update_formula,
    x_initial,
    y_initial,
    z_initial,
    total_time,
    step_size,
):
    initial_conditions = np.array(
        [
            x_initial,
            y_initial,
            z_initial,
        ]
    )

    solver = Solver([x_update_formula, y_update_formula, z_update_formula])
    _, x, _ = solver.integrate(initial_conditions, step_size, total_time)
    df = pd.DataFrame(
        {
            "x": x[0, :],
            "y": x[1, :],
            "z": x[2, :],
        }
    )

    fig = px.line_3d(df, x="x", y="y", z="z")

    return fig


@app.callback(
    Output(component_id="x_update_formula", component_property="value"),
    Output(component_id="y_update_formula", component_property="value"),
    Output(component_id="z_update_formula", component_property="value"),
    Input(component_id="dyanamic_system_key", component_property="value"),
)
def update_system(dynamic_system_key):
    return (
        SYSTEMS[dynamic_system_key][0],
        SYSTEMS[dynamic_system_key][1],
        SYSTEMS[dynamic_system_key][2],
    )


if __name__ == "__main__":
    app.run_server(debug=True)

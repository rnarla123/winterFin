#dash libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State


#yahoo finance
import yfinance as yf


#plotly libraries
import plotly.figure_factory as ff
import plotly.graph_objects as go
import plotly.express as px
import plotly.offline as py
from plotly.offline import download_plotlyjs, init_notebook_mode, plot


from stock import get_stock


form = dbc.Form(
    [
        dbc.FormGroup(
            [
                dbc.Label("Enter Stock", className="mr-2"),
                dbc.Input(id='input', value='', type='text', placeholder="Name"),
            ],
            className="mr-3",
            style={'padding-bottom':'2vh'}
        ),
        html.Br(),
        dbc.Button("Graph", color="primary", block=True, id="graph-button"),
        dbc.Button("Perform Prediction", color="primary", id="predict-button", block=True),
    ],
    inline=True,
)


first_card = dbc.Card(
    dbc.CardBody(
        [
            dbc.CardHeader("Stocks Analysis"),
            html.Br(),
            form,
        ]
    ),
    style={'height':'100vh'}
)


second_card = dbc.Card(
    dbc.CardBody(
        [
            dbc.CardHeader("Graphs"),
            html.Div(id='output-graph'),
        ]
    ),
    style={'height':'100vh'}
)


cards = dbc.CardGroup([dbc.Col(first_card, width=3), dbc.Col(second_card, width=9)])


app = dash.Dash(external_stylesheets=[dbc.themes.DARKLY])
app.layout = html.Div(cards)


@app.callback(
    Output(component_id='output-graph', component_property='children'),
    [
        Input(component_id="graph-button", component_property="n_clicks")
    ],
    state=[
        State(component_id='input', component_property='value'),
    ]
)
def update_value(n_clicks, input_value):
    if input_value and n_clicks:
        stock = get_stock(input_value, '10y')

        return dcc.Graph(
            id='example-graph',
            figure=stock[1]
        )

if __name__ == '__main__':
    app.run_server(debug=True)
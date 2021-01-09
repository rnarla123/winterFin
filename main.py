#dash libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


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
        ),
        html.P("Click:"),
        html.Br(),
        dbc.Button("Graph", color="primary", block=True, id="graph-button"),
        dbc.Button("Perform Analysis", color="primary", block=True),
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
        Input(component_id='input', component_property='value'), 
        Input(component_id="graph-button", component_property="n_clicks")
    ]
)
def update_value(input_data, n):
    if input_data and n:
        stock = get_stock(input_data, '10y')

        return dcc.Graph(
            id='example-graph',
            figure=stock[1]
        )


if __name__ == '__main__':
    app.run_server(debug=True)
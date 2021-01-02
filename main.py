#dash libraries
import dash
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

app = dash.Dash()

app.layout = html.Div(children=[
    html.Div(children='''
        Symbol to graph:
    '''),
    dcc.Input(id='input', value='', type='text'),
    html.Div(id='output-graph'),
])


@app.callback(
    Output(component_id='output-graph', component_property='children'),
    [Input(component_id='input', component_property='value')]
)
def update_value(input_data):
    if input_data:
        stock = get_stock(input_data, '10y')

        return dcc.Graph(
            id='example-graph',
            figure=stock[1]
        )


if __name__ == '__main__':
    app.run_server(debug=True)
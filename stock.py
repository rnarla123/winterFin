#yahoo finance
import yfinance as yf


#plotly libraries
import plotly.figure_factory as ff
import plotly.graph_objects as go
import plotly.express as px
import plotly.offline as py
from plotly.offline import plot


def get_stock(stock_name, period='max'):
    stock = yf.Ticker(stock_name)
    hist = stock.history(period=period)
    if len(hist):
        hist = hist.reset_index()
        
        avg_14 = hist.Open.rolling(window=14, min_periods=1).mean()
        avg_21 = hist.Open.rolling(window=21, min_periods=1).mean()
        avg_100 = hist.Open.rolling(window=100, min_periods=1).mean()
        
        fig = go.Figure()
        
        temp = hist.tail(int(0.25*len(hist)))
        
        fig.add_trace(go.Ohlc(x=hist['Date'],
                              open=hist['Open'],
                              high=hist['High'],
                              low=hist['Low'],
                              close=hist['Close'], 
                              name=stock_name))
        
        fig.add_trace(go.Candlestick(x=hist['Date'],
                              open=hist['Open'],
                              high=hist['High'],
                              low=hist['Low'],
                              close=hist['Close'], 
                              name=stock_name, 
                              visible='legendonly'))
        
        fig.add_trace(go.Scatter(x=hist['Date'], y=hist['Open'], name='Open',
                         line=dict(color='royalblue', width=1.5), visible='legendonly'))
        
        fig.add_trace(go.Scatter(x=hist['Date'], y=hist['Close'], name = 'Close',
                         line=dict(color='firebrick', width=1.5), visible='legendonly'))
        
        fig.add_trace(go.Scatter(x=hist['Date'], y=avg_14, name = '14 Day Close Avg',
                         line=dict(color='goldenrod', width=1.5), visible='legendonly'))
        
        fig.add_trace(go.Scatter(x=hist['Date'], y=avg_21, name = '21 Day Close Avg',
                                 line=dict(color='orangered', width=1.5), visible='legendonly'))
        
        fig.add_trace(go.Scatter(x=hist['Date'], y=avg_100, name = '100 Day Close Avg',
                                 line=dict(color='mediumorchid', width=1.5), visible='legendonly'))

        fig.update_layout(xaxis_title='Date', yaxis_title='Price', template="plotly_dark")
        
        fig.update_layout(
            updatemenus=[
                dict(buttons=list([
                     dict(label = 'OHLC Plot',
                          method = 'update',
                          args = [{'visible': [True, False, False, False, False, False, False]},
                                  {'title': 'OHLC Plot for ' + stock_name,
                                   'showlegend':True}]),
                     dict(label = 'Candlestick Plot',
                          method = 'update',
                          args = [{'visible': [False, True, False, False, False, False, False]},
                                  {'title': 'Candlestick Plot for ' + stock_name,
                                   'showlegend':True}]),
                     dict(label = 'Open Price',
                          method = 'update',
                          args = [{'visible': [False, False, True, False, False, False, False]},
                                  {'title': 'Open Price for ' + stock_name,
                                   'showlegend':True}]),
                     dict(label = 'Close Price',
                          method = 'update',
                          args = [{'visible': [False, False, False, True, False, False, False]},
                                  {'title': 'Close Price for ' + stock_name,
                                   'showlegend':True}]),
                     dict(label = '14 Day Moving Average',
                          method = 'update',
                          args = [{'visible': [False, False, False, False, True, False, False]},
                                  {'title': '14 Day Moving Average for Open Price of ' + stock_name,
                                   'showlegend':True}]),
                    dict(label = '21 Day Moving Average',
                          method = 'update',
                          args = [{'visible': [False, False, False, False, False, True, False]},
                                  {'title': '14 Day Moving Average for Open Price of ' + stock_name,
                                   'showlegend':True}]),
                    dict(label = '100 Day Moving Average',
                          method = 'update',
                          args = [{'visible': [False, False, False, False, False, False, True]},
                                  {'title': '100 Day Moving Average for Open Price of ' + stock_name,
                                   'showlegend':True}]),
                    dict(label = 'Open, Close, 14, 21, 100',
                          method = 'update',
                          args = [{'visible': [False, False, True, True, True, True, True]},
                                  {'title': 'All Line Plots for ' + stock_name,
                                   'showlegend':True}]),
                    ]), 
                    direction="down",
                    pad={"r": 10, "t": 10},
                    showactive=True,
                    x=0.1,
                    xanchor="left",
                    y=1.1,
                    yanchor="top"
                ),
            ]
        )
        
        fig.update(layout_xaxis_rangeslider_visible=False)
        return hist, fig
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
        fig = go.Figure()
        
        temp = hist.tail(int(0.25*len(hist)))
        
        fig.add_trace(go.Ohlc(x=temp['Date'],
                        open=temp['Open'],
                        high=temp['High'],
                        low=temp['Low'],
                        close=temp['Close'], name=stock_name))

        fig.update_layout(title='OHLC Plots for ' + stock_name,
                           xaxis_title='Date',
                           yaxis_title='Ticks', template="plotly_dark")

        fig.update(layout_xaxis_rangeslider_visible=False)
        return hist, fig
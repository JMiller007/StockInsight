from flask import Flask, render_template, request
import yfinance as yf
import plotly.graph_objs as go
import plotly.io as pio

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    stock_data = None
    if request.method == 'POST':
        stock_symbol = request.form['stock_symbol']
        stock_data = fetch_stock_data(stock_symbol)
    return render_template('index.html', stock_data=stock_data)

@app.route('/investing')
def investing():
    return render_template('investing.html')

@app.route('/stocks')
def stocks():
    return render_template('stocks.html')

def fetch_stock_data(symbol):
    stock = yf.Ticker(symbol)
    hist = stock.history(period="1y")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=hist.index, y=hist['Close'], mode='lines', name='Close Price'))
    fig.update_layout(title=f'Stock Prices for {symbol.upper()}', xaxis_title='Date', yaxis_title='Price')
    graph_html = pio.to_html(fig, full_html=False)
    return graph_html

if __name__ == '__main__':
    app.run(debug=True)

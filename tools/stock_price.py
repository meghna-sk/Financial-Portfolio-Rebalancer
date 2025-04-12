import yfinance as yf
from langchain.tools import Tool
from utils.logger import log_tool_usage

def get_stock_price(symbol):
    try:
        log_tool_usage("MarketTrendAnalyzer")
        stock = yf.Ticker(symbol)
        data = stock.history(period="1d")
        if data.empty:
            return f"No data found for {symbol}"
        close = data["Close"].iloc[-1]
        return f"{symbol.upper()} latest price: ${round(close, 2)}"
    except Exception as e:
        return f"Error retrieving stock price: {str(e)}"

stock_price_tool = Tool(
    name="StockPriceLookup",
    func=get_stock_price,
    description="Gets current price of a stock. Input should be a stock symbol."
)
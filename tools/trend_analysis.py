import yfinance as yf
from langchain.tools import Tool
from utils.logger import log_tool_usage

def market_trend_analysis(_input=None):
    """
    Fetches stock market index trends over the past week.
    Returns a summary of the S&P 500 movement and volatility.
    """
    try:
        log_tool_usage("MarketTrendAnalyzer")
        spy = yf.Ticker("SPY")
        hist = spy.history(period="7d")
        if hist.empty or len(hist) < 2:
            return "Not enough data to analyze market trend."

        start_price = hist["Close"].iloc[0]
        end_price = hist["Close"].iloc[-1]
        change_pct = ((end_price - start_price) / start_price) * 100

        volatility = hist["Close"].pct_change().std() * (252 ** 0.5) * 100

        return (
            f"S&P 500 (SPY) 5-day return: {round(change_pct, 2)}%\n"
            f"Annualized volatility: {round(volatility, 2)}%"
        )

    except Exception as e:
        return f"Error analyzing market trends: {str(e)}"

trend_tool = Tool(
    name="MarketTrendAnalyzer",
    func=market_trend_analysis,
    description="Provides an analysis of recent market trends. No input required."
)
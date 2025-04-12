from langchain.tools import Tool
from utils.logger import log_tool_usage

def rebalance_portfolio(portfolio_str):
    try:
        log_tool_usage("PortfolioRebalancer")
        portfolio = eval(portfolio_str)
        n = len(portfolio)
        target = 1 / n
        result = []
        for symbol, weight in portfolio.items():
            delta = round(weight - target, 4)
            action = "Sell" if delta > 0 else "Buy" if delta < 0 else "Hold"
            result.append(f"{action} {symbol}: {abs(round(delta * 100, 2))}%")
        return "\n".join(result)
    except Exception as e:
        return f"Error analyzing portfolio: {str(e)}"

rebalance_tool = Tool(
    name="PortfolioRebalancer",
    func=rebalance_portfolio,
    description="Suggests actions to balance a portfolio equally."
)
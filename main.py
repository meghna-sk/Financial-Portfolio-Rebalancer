import time
from agents.llm_selector import get_llm
from tools.stock_price import stock_price_tool
from tools.rebalance import rebalance_tool
from tools.trend_analysis import trend_tool
from langchain.agents import initialize_agent, AgentType
from utils.logger import get_tool_log, reset_tool_log

# Toggle verbosity to see full tool trace (Thought → Action → Observation)
VERBOSE_MODE = True

def create_and_run_agent(llm_provider="claude", llm_model="default", query=""):
    llm = get_llm(llm_provider, llm_model)
    tools = [stock_price_tool, rebalance_tool, trend_tool]

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=VERBOSE_MODE
    )

    # Reset tool usage log and start timing
    reset_tool_log()
    start_time = time.time()
    response = agent.run(query)
    end_time = time.time()

    # Metrics
    latency = round(end_time - start_time, 2)
    tools_used = get_tool_log()
    unique_tools = set(tools_used)

    print(f"\nLatency for {llm_provider.upper()} ({llm_model}): {latency} seconds")
    print(f"Tools used: {tools_used}")
    print(f"Total tool calls: {len(tools_used)}")
    print(f"Unique tools used: {unique_tools}\n")

    return response

def run_test_cases():
    portfolio_1 = {"AAPL": 0.5, "TSLA": 0.3, "GOOGL": 0.2}
    portfolio_2 = {"MSFT": 0.25, "NVDA": 0.25, "AMZN": 0.25, "META": 0.25}

    test_cases = [
        ("claude", "default"),
        ("groq", "llama3-8b"),
        ("groq", "llama3-70b")
    ]

    for provider, model in test_cases:
        print(f"\n============================")
        print(f"MODEL: {provider.upper()} - {model.upper()}")
        print("============================")

        print("\nPortfolio 1:")
        print(create_and_run_agent(provider, model, f"Analyze this portfolio and recommend changes: {portfolio_1}"))

        print("\nPortfolio 2:")
        print(create_and_run_agent(provider, model, f"Analyze this portfolio and recommend changes: {portfolio_2}"))

    print("\nAll test cases completed.\n")

if __name__ == "__main__":
    run_test_cases()

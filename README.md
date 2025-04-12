# AI-Powered Financial Portfolio Rebalancer (Multi-LLM Agent)

This project implements an AI assistant using LangChain that analyzes and suggests adjustments to a stock portfolio based on real-time market data. It integrates multiple LLMs (Claude 3 Opus, Groq LLaMA3-8B, and LLaMA3-70B) and dynamically selects tools to evaluate the user's portfolio and recommend rebalancing actions.

## Features

- Retrieves live stock prices using Yahoo Finance
- Analyzes portfolio imbalances using an equal-weight strategy
- Recommends rebalancing actions (Buy / Sell / Hold)
- Provides contextual market trend analysis
- Supports multiple LLM providers via LangChain agents
- Tracks response latency and tool selection efficiency

## Tech Stack

- Python 3.10+
- LangChain (Agent Framework)
- yfinance (Stock Data)
- Anthropic Claude 3 (via langchain-anthropic)
- Groq LLaMA3 (8B and 70B models)
- Pandas, Requests, Dotenv

## Project Structure

├── main.py                    # Entry point for agent execution and testing
├── agents/
│   └── llm_selector.py        # Multi-LLM selection and configuration
├── tools/
│   ├── stock_price.py         # Stock price lookup tool
│   ├── rebalance.py           # Portfolio rebalancing logic
│   └── trend_analysis.py      # Market trend analysis
├── utils/
│   └── logger.py              # Tracks tool usage for evaluation
├── .env                       # (Not included) Stores your API keys
└── requirements.txt           # Python package dependencies

Setup Instructions

1. Clone the Repository

git clone https://github.com/your-username/portfolio-rebalancer-ai.git
cd portfolio-rebalancer-ai

2. Create and Activate a Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies

pip install -r requirements.txt

4. Create a .env File

In the root directory, create a `.env` file and add the following:

ANTHROPIC_API_KEY=your_claude_api_key_here
GROQ_API_KEY=your_groq_api_key_here

## Running the Project

Run the project with:

python main.py

This will:
- Analyze two sample portfolios using three different LLMs
- Print results, latency, and tool usage
- Help compare model performance

Evaluation Metrics

This assistant was tested on the following:
- Response Accuracy
- Response Time / Latency
- Tool Selection Efficiency
- Quality of Financial Advice

See CO3_msurajka.pdf for a complete analysis and model comparison.

Submission Notes

- API keys removed from all shared code
- `.env` excluded from GitHub/ZIP submission
- Technical report included as PDF
- All scripts independently runnable

## Author
Created for the Agent-Based Modeling and Agentic Technology course (Spring 2025).  
Assignment: AI Financial Assistant using LangChain Agents.
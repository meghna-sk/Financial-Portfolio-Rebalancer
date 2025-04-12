import os
from utils.env_loader import load_env_vars
from langchain_anthropic import ChatAnthropic
from langchain_groq import ChatGroq

load_env_vars()

claude_llm = ChatAnthropic(
    model="claude-3-opus-20240229",  # You can use claude-3-sonnet too
    temperature=0,
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

groq_llm_llama3_8b = ChatGroq(
    model_name="llama3-8b-8192",
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY")
)

groq_llm_llama3_70b = ChatGroq(
    model_name="llama3-70b-8192",
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY")
)

def get_llm(provider="claude", model="default"):
    if provider.lower() == "claude":
        return claude_llm
    elif provider.lower() == "groq":
        return groq_llm_llama3_70b if model.lower() == "llama3-70b" else groq_llm_llama3_8b
    else:
        return claude_llm
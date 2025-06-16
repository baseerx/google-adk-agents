from google.adk.agents import Agent
import yfinance as yf
from google.adk.tools import google_search

# This code creates a basic agent and a tool agent using the Google ADK library.
#agent name and project name should be same
basic_agent = Agent(
    model='gemini-2.0-flash-001',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
)


#1.Creating basic agent with built-in tools
google_search_agent=Agent(
    model='gemini-2.0-flash-001',
    name='google_search_agent',
    description='A helpful assistant for user questions with Google Search.',
    instruction='Answer user questions to the best of your knowledge using Google Search.',
    tools=[google_search]
)

#2.Creating tool agent
#multi line comments inside tool function allows agent to understand the purpose of the tool
def get_stock_price(ticker: str) -> dict:
    """
    Get the current stock price for a given ticker symbol. this is tool and will be used by the agent to fetch stock prices.
    """
    stock = yf.Ticker(ticker)
    price = stock.info.get('currentPrice', "Price not available")
    return {"price": price, "ticker": ticker}

def name_of_agent() -> str:
    """
    This is a tool function that returns the name of the agent.
    """
    return "This agent is named 'Baseer'."

instruction=""

try:
    instruction = open('instructions.txt', 'r').read()
except FileNotFoundError:
    instruction = "Use this agent to get stock prices for a given ticker symbol."

tool_agent = Agent(
    model='gemini-2.0-flash-001',
    name='tool_agent',
    description='A tool agent for fetching stock prices.',
    instruction=instruction,
    tools=[get_stock_price, name_of_agent]
)

print(instruction)

# Assigning the tool agent to the root agent, root_agent decides which agent to use
root_agent = google_search_agent

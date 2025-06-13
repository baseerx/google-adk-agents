from google.adk.agents import Agent
import yfinance as yf

basic_agent = Agent(
    model='gemini-2.0-flash-001',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
)


#2.Creating tool agent

def get_stock_price(ticker: str) -> float:
    """
    Get the current stock price for a given ticker symbol. this is tool and will be used by the agent to fetch stock prices.
    """
    stock = yf.Ticker(ticker)
    price = stock.info.get('currentPrice', "Price not available")
    return {"price": price, "ticker": ticker}

tool_agent = Agent(
    model='gemini-2.0-flash-001',
    name='tool_agent',
    description='A tool agent for fetching stock prices.',
    instruction='Use this agent to get stock prices for a given ticker symbol.',
    tools=[get_stock_price]
)

root_agent = tool_agent
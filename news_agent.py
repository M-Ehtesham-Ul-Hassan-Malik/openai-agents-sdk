from dotenv import load_dotenv
import os
from agents import Agent, function_tool, Runner, WebSearchTool

load_dotenv()  

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable not set.")

news_agent = Agent(
    name="News Agent",
    instructions=
    """
    You are a news agent that can search the web for the latest news on the given topic.
    Compile the information you find into a single paragraph concise summary. No markdown, just plain text.
    """,
    tools=[WebSearchTool()]
)

while True:
    query = input("Enter a topic to search for news (or 'exit' to quit): ")
    if query.lower() == 'exit':
        break
    result = Runner.run_sync(news_agent, query)
    print("\nResult:")
    print(result.final_output)
    print("\n" + "="*50 + "\n")
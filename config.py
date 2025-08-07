from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig
import os

# Get Gemini API Key from .env
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY is not set. Please check your .env file.")

# Create OpenAI-compatible Gemini client
external_client = AsyncOpenAI(
    api_key=GOOGLE_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Create model object
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

# Create config for running the agent
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

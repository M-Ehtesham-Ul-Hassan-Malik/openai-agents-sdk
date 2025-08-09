import chainlit as cl
from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig, Runner
from dotenv import load_dotenv
import os

load_dotenv()

# Step 1: Provider 
provider = AsyncOpenAI(
    api_key=os.getenv("Google_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Step 2: Model
model = OpenAIChatCompletionsModel(
    openai_client=provider,
    model="gemini-2.5-flash",
)

# Step 3: Run level config 
config = RunConfig(
    model = model,
    model_provider = provider,
    tracing_disabled = True,
)

# Step 4: Create an agent
agent = Agent(
    name="simple agent",
    instructions="You are a helpful assistant that can answer user questions.",
    model=model
)

# result = Runner.run_sync(agent, "Hello, Who is the Founder of Pakistan?", run_config=config)
# print(result.final_output)

@cl.on_chat_start
async def start_chat():
    cl.user_session.set("history", [])
    await cl.Message(content="Hello! I am your assistant. How can I help you today?").send()


@cl.on_message
async def handle_msg(message: str):
    history = cl.user_session.get("history", [])

    # standard interface [{"role": "user", "content": message.content}]
    history.append({"role": "user", "content": message.content})



    result = await Runner.run(
        starting_agent=agent,
        input=history,
        run_config=config
    )
    history.append({"role": "assistant", "content": result.final_output})
    cl.user_session.set("history", history)
    await cl.Message(content=result.final_output).send()





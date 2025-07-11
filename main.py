from agents import Runner, Agent, OpenAIChatCompletionsModel, AsyncOpenAI, RunConfig
import os
from dotenv import load_dotenv
from tools import get_flights, suggest_hotels

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client,
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True,
)

destination_agent = Agent(
    name="DestinationAgent",
    instructions="""
    Based on the user's mood or interest (e.g., beach, adventure, history), recommend **ONE** best-fit destination. 
    Keep the response to **just the destination name** (e.g., 'Bali' or 'Rio de Janeiro'). Do not ask questions or provide lists.
    """,
)

booking_agent = Agent(
    name="BookingAgent",
    instructions="Based on the destination, suggest flight and hotel options.",
    tools=[get_flights, suggest_hotels],
)

explore_agent = Agent(
    name="ExploreAgent",
    instructions="""
    You're a travel guide assistant. When given a destination, suggest top attractions and popular food places.
    Example: For 'Tokyo', suggest places like Shibuya Crossing, Senso-ji Temple, and dishes like sushi or ramen.
    """,
)

def main():
    print("🌍 AI Travel Agent\n")
    interest = input("Tell me your travel mood or interest (e.g., beach, adventure, culture): ").strip().lower()

    result1 = Runner.run_sync(
        destination_agent,
        interest,
        run_config=config
    )
    destination = result1.final_output.strip()
    print("\nSuggested Destination:", destination)

    result2 = Runner.run_sync(
        booking_agent,
        destination,
        run_config=config
    )
    print("\nFlight & Hotel Options:", result2.final_output)

    result3 = Runner.run_sync(
        explore_agent,
        destination,
        run_config=config
    )
    print("\nAttractions & Food Suggestions:", result3.final_output)

if __name__ == "__main__":
    main()

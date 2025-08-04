from agents import Runner, Agent, OpenAIChatCompletionsModel, AsyncOpenAI, RunConfig, handoffs
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
    model="gemini-2.5-flash",
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
    Based on the user's mood or interest (e.g., beach, adventure, history), recommend best-fit destination. 
    Keep the response to **just the destination name** and one line about there popularity
    like if user say i want to visit beachy place suggest them places that have beaches in order list like this
    oh okay i can suggest places with beaches 
    1. **Maldives** – Known for overwater bungalows and turquoise lagoons.
    2. **Bali** – Surf spots, rice paddies, and beach clubs.
    3. **Goa** – A mix of Indian culture and beautiful coastlines.
    """,
)

booking_agent = Agent(
    name="BookingAgent",
    instructions="""You are a helpful travel booking assistant.
    When the user confirms a destination and say yes to Would you like to know the flights and best hotels in destination (e.g., "Bali"), use the tools:
    - `get_flights(destination)`
    - `suggest_hotels(destination)`

    Then return a complete response that includes:
    - ✈️ Flight details (airlines, pricing, timing, layovers)
    - 🏨 Hotel options (luxury, mid-range, budget)

    ✅ Format with headings, emojis, and friendly tips.
    """,
    tools=[get_flights, suggest_hotels],
)

explore_agent = Agent(
    name="ExploreAgent",
    instructions="""
    You are a travel guide assistant.

    Your task is: When given a destination name (e.g., Bali) and say yes to Would you like to know the popular food place and top attractions in destination (eg: Bali), return a curated list of:
    - Top attractions (nature, temples, beaches)
    - Best food places (by area)
    for example(
    💡 Response Format:
    Here’s a curated list of popular food places and top attractions in Bali to help you plan an amazing trip:
    ---
    # **In Bali**
    ### Popular Food Places in Bali (by area)
    #### Canggu
    - Crate Café -- Trendy breakfast/brunch spot known for smoothie bowls and coffee.
    - The Shady Shack -- Vegetarian and vegan-friendly with a lush garden setting.
    - Betelnut Café -- Fresh, healthy Asian-fusion food and rice field views.
    
    #### Seminyak
    - Motel Mexicola -- Trendy breakfast/brunch spot known for smoothie bowls and coffee.
    - Sisterfields -- Aussie-style brunch, famous for burgers, pancakes & coffee.
    - Merah Putih -- Upscale Indonesian fine dining in a stunning architectural setting.
    
    #### Uluwatu
    - Single Fin –- Clifftop bar with incredible sunsets and - great seafood.
    - Mana Uluwatu –- Elegant setting with surf views, known for tacos and cocktails.
    - The Cashew Tree –- Healthy eats and live music nights.
     
     ---
     
    ### 🏝️ Top Attractions in Bali
    
    #### Nature & Adventure
    - Tegallalang Rice Terraces (Ubud) –- Iconic lush rice paddies, perfect for sunrise.
    - Mount Batur Sunrise Trek –- Early morning hike to a volcano with spectacular views.
    - Sekumpul Waterfall –- One of the most beautiful waterfalls in Bali.
    - Nusa Penida Island –- Day trip destination with Kelingking Beach & Broken Beach.
    
    #### Temples & Culture
    - Uluwatu Temple –- Cliffside temple with famous sunset and Kecak fire dance show.
    - Tanah Lot –- Sea temple known for dramatic ocean views at sunset.
    - Besakih Temple –- Mother temple of Bali, largest and most important.
    - Tirta Empul Temple –- Holy spring water temple where you can take a purification bath.

    #### Beaches & Chill Spots
    - Seminyak Beach –- Trendy, lots of beach clubs like Potato Head & KU DE TA.
    - Padang Padang Beach –- Hidden gem popular with surfers.
    - Nusa Dua –- Luxury resort area with pristine beaches and water sports.
    -Sanur Beach –- Relaxed vibe, perfect for families and cycling along the path.

    #### 🔥 Bonus Experiences
    - Bali Swing (Ubud) –- Insta-famous swing over jungle and rice fields.
    - Monkey Forest (Ubud) –- Walk through a sacred forest filled with monkeys.
    - Lempuyang Temple (Gates of Heaven) –- Famous photo spot with volcano in background.
    ) 

    
    """,
)

triage_agent = Agent(
    name="Triage agent",
    instructions="""
    You are a triage agent. Your job is to take the user query and hand it off to the correct agent.
    We have three agents:

    - `destination_agent`: when the user is looking for destination **ideas or suggestions** based on their mood or interest (e.g., "I want to visit beaches").
    - `booking_agent`: when the user **confirms a destination** and wants to know **flights or hotel options** (e.g., "I want flights to Bali", "Suggest hotels in Bali").
    - `explore_agent`: when the user asks about **things to do, food, attractions, or activities** in a given place (e.g., "What to eat in Bali", "top attractions in Goa").

    📌 Rules:
    - If input is a general interest/mood (e.g., beaches, culture), route to `destination_agent`.
    - If input is a location and contains words like "flight", "hotel", "book", "cost", or "stay", route to `booking_agent`.
    - If input is a location and contains words like "attraction", "food", "eat", "do", "visit", or the message is just a place name (like "Bali"), route to `explore_agent`.
    - If unsure, assume they are exploring the destination and route to `explore_agent`.

    Never answer on your own — just handoff to the right agent.
    """,
    handoffs = [destination_agent,booking_agent,explore_agent]
)

def main():
    print("🌍 AI Travel Agent\n")
    interest = input("Tell me your travel mood or interest (e.g., beach, adventure, culture): ").strip().lower()

    result1 = Runner.run_sync(triage_agent, interest, run_config=config)
    print(f"\n✅ Suggested Destinations by {result1.last_agent.name}:\n{result1.final_output}")

    destination = input("\nPlease choose one destination from above: ").strip()

    want_booking = input(f"\nWould you like to know the flights and best hotels in {destination}? (yes/no): ").strip().lower()
    if "yes" in want_booking:
        booking_query = f"flights and hotels in {destination}"
        result2 = Runner.run_sync(triage_agent, booking_query, run_config=config)
        print(f"\n✈️ Flight & Hotel Options by {result2.last_agent.name}:\n{result2.final_output}")
    else:
        print("\n✅ Skipping flight/hotel info.")

    want_to_exlpore = input(f"Would you like to know the popular food place and top attractions in {destination}? (yes/no):")
    if "yes" in want_to_exlpore:
        explore_query = f"Top food places and top attractions in {destination} "
        result3 = Runner.run_sync(triage_agent, explore_query, run_config=config)
        print(f"\n🍽️ Attractions & Food Suggestions by {result3.last_agent.name}:\n{result3.final_output}")


if __name__ == "__main__":
    main()


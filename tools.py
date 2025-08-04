from agents import function_tool

@function_tool
def get_flights(destination: str) -> str:
    return f"""
**Flights to {destination.title()}**

✈️ *Sample Flight Info*:  
- One-way fares: ~USD 220–300 (based on season and airline)  
- Typical journey time: 16–24 hours with 1–2 layovers  
- Popular airlines: AirAsia, Emirates, Qatar Airways, SriLankan Airlines  
- Layovers may include: Kuala Lumpur, Dubai, Doha, Bangkok

💡 *Booking Tips*:  
- Book 4–8 weeks in advance for better fares  
- Cheapest days: Sundays, Tuesdays, and Wednesdays  
    """
    

  

@function_tool
def suggest_hotels(destination: str) -> str:
    return f"""
🏨 **Top Hotel Picks in {destination.title()}**

**Luxury & Upscale**  
- [Hotel One] – 5-star beachfront resort with spa and private pool  
- [Hotel Two] – Clifftop villa with infinity pool and panoramic views

**Mid-Range & Boutique**  
- [Hotel Three] – Cozy boutique stay near downtown  
- [Hotel Four] – Family-friendly resort with included breakfast

**Budget-Friendly**  
- [Hotel Five] – Clean and comfy, great reviews, ~USD 40–60/night  
- [Hostel Six] – Social vibe with shared dorms and events

💡 *Note*: Most hotels offer free cancellation. Book early for peak seasons!
    """
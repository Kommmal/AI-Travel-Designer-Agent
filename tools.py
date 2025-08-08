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

**Ultimate Luxury Retreats**  
- Mandapa, a Ritz‑Carlton Reserve – Exceptional resort with lush surroundings  
- The Mulia – Luxurious Nusa Dua beachfront resort with exquisite service  
- The Ritz‑Carlton, Bali – Elegant luxury with beachfront access  
- Four Seasons Resort Bali at Jimbaran Bay – Iconic luxury and privacy  
- The Apurva Kempinski Bali – Cliffside indulgence with aquarium-themed dining

**Wellness & Nature-Immersed Escapes**  
- COMO Shambhala Estate – Serene wellness retreat in Ubud jungle  
- Capella Ubud – Tented luxury with immersive nature experience  
- Buahan – Boutique, open-air design near Ubud blending indoors and outdoors

**Trendy Beachfront & Design-Focused Stays**  
- Potato Head Suites & Studios, Seminyak – Eco-conscious design and vibrant nightlife  
- W Bali – Seminyak – Energetic oceanfront with upscale dining and beach bars

**Boutique & Mid-Range Options**  
- Viceroy Bali, Ubud – Private villas, spa, and river views  
- Hotel Tugu Bali, Canggu – Historical charm and Balinese aesthetics  
- Nadi Nature Resort – Budget stay with nature focus  
- Maua Nusa Penida – Affordable guesthouse with island access  
- Mathis Lodge Amed – Budget beachfront lodging  
- The Royal Purnama – Mid-range beachfront resort  
- The Bohemian Bali – Budget boutique vibe

**All-Inclusive Convenience**  
- The Melia Bali, Nusa Dua – Family-friendly all-inclusive resort  
- Samabe Bali Suites & Villas – Luxury all-inclusive with spa and kids’ club  
- Grand Mirage Resort & Thalasso – Beach resort with all amenities  
- Club Med Bali – Comprehensive all-inclusive experience  
- Spa Village Resort – Wellness-focused all-inclusive retreat  
- Escape Haven – Relaxing all-inclusive beachfront stay

💡 *Note*: Many Bali hotels offer free cancellation and peak season bookings fill fast!
    """

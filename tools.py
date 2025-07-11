from agents import function_tool

@function_tool
def get_flights(destination: str) -> str :
    return f"✈️ Flights to {destination} found: Economy - $450, Business - $950"



@function_tool
def suggest_hotels(destination: str) -> str:
    return f"🏨 Suggested Hotels in {destination}: Luxe Inn, Ocean View, Budget Stay"

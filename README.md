# 🧠 AI Travel Designer Agent

**AI Travel Designer Agent** is an intelligent assistant built using the OpenAI `agents` SDK. It coordinates between multiple specialized agents to create a personalized travel experience based on the user's mood or interest (like beach, adventure, or culture).

---

## ✨ Features

- 💡 Suggests a travel destination based on user mood or preference
- ✈️ Provides mock flight and hotel options using custom tools
- 🗺️ Recommends top attractions and local food spots for the destination
- 🧠 Modular agent-based system using OpenAI Agent SDK
- 🧰 Tool integrations for mock data generation

---

## 🧩 How It Works

The assistant uses three core agents working in a sequence:

| Agent | Role |
|-------|------|
| **DestinationAgent** | Suggests a destination based on the user's interest |
| **BookingAgent**     | Provides mock flights and hotel options using tools |
| **ExploreAgent**     | Recommends attractions and food at the destination |

Each agent is powered by OpenAI or Gemini models using the `agents` SDK and runs with a shared configuration to maintain context.

---

## ⚙️ Tech Stack

- **Python**
- **OpenAI Agents SDK**
- **Gemini API** (for LLM model)
- **`uv`** (for virtual environment & running the app)
- **Tools**: `get_flights`, `suggest_hotels`

---

## 🚀 Quick Start

1. **Clone the repository**

   ```bash
   git clone https://github.com/Kommmal/AI-Travel-Designer-Agent.git
   cd AI-Travel-Designer-Agent

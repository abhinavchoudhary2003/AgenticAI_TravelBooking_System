# 🌍 AgenticAI Travel Booking System

An intelligent, autonomous Multi-Agent AI System built using **LangGraph** to streamline and automate the entire travel planning and booking experience. The system coordinates 4 specialized AI agents that collaborate autonomously to generate complete, personalized travel packages.

---

## 🚀 Key Features

* **Multi-Agent Orchestration:** Decomposes complex travel requests into 4 collaborative, specialized agents:
  * ✈️ **Flight Search Agent:** Discovers live flights, routes, and schedules using real-time aviation APIs.
  * 🏨 **Hotel Search Agent:** Identifies lodging options tailored to the destination, budget constraints, and user preferences.
  * 🗓️ **Itinerary Planning Agent:** Generates day-by-day itineraries, balancing sightseeing, activities, and dining.
  * 🤖 **Final Response Agent:** Consolidates and refines outputs from all agents into a unified, actionable travel plan.
* **🧠 Persistent Memory via PostgreSQL:** Utilizes PostgreSQL checkpoints (`langgraph-checkpoint-postgres`) to maintain multi-turn conversational context, state, and travel preferences across interactions.
* **🌐 Real-Time API Integration:** Connects with live search and travel data feeds to fetch current pricing, availability, and local attraction details.
* **💻 Interactive Streamlit Interface:** Provides a conversational web UI that enables users to easily view, refine, and modify generated itineraries in real time.

---

## 🛠️ Tech Stack

* **Language:** Python 3.10+
* **Agent Orchestration:** LangGraph, LangChain
* **LLM & Inference:** Llama 3.3 70B via Groq
* **State & Memory Management:** PostgreSQL (`psycopg`, `langgraph-checkpoint-postgres`)
* **User Interface:** Streamlit
* **External APIs & Tools:**
  * **Search & Web Intelligence:** Tavily API
  * **Flight Data:** AviationStack API

---

## 📂 Project Structure

```text
AgenticAI_TravelBooking_System/
│
├── agents/             # Autonomous agent definitions and prompt templates
├── tools/              # API wrappers and custom search/booking tools
├── config/             # Environment variables and system configurations
├── app.py              # Main application entry point / CLI backend
├── frontend.py         # Streamlit web application interface
├── requirements.txt    # Project dependencies
└── README.md           # Documentation
```

---

## 🔄 Project Workflow

```text
User Request ──► [Flight Agent] ──► [Hotel Agent] ──► [Itinerary Agent] ──► [Final Response Agent]
                         ▲               ▲                    ▲                    │
                         └───────────────┴────────────────────┴────────────────────┘
                                        PostgreSQL Memory Checkpointer
```

* **Flight Agent:** Searches available flights using AviationStack.
* **Hotel Agent:** Searches accommodations matching the destination and budget using Tavily search.
* **Itinerary Agent:** Creates a tailored daily sightseeing and activity schedule.
* **Final Response Agent:** Synthesizes the information into a single structured recommendation.
* **PostgreSQL Checkpointer:** Stores states and memory for seamless multi-turn conversations.

---

## ⚙️ Installation & Setup

Follow the steps below to set up and run the project locally.

### Step 1: Clone the Repository

```bash
git clone https://github.com/abhinavchoudhary2003/AgenticAI_TravelBooking_System.git
cd AgenticAI_TravelBooking_System
```

### Step 2: Create and Activate a Virtual Environment

Open your terminal in the project directory and run:

```bash
python -m venv langgraph_env3
```

Activate the environment:

**Windows:**

```dos
langgraph_env3\Scripts\activate
```

**macOS / Linux:**

```bash
source langgraph_env3/bin/activate
```
### Step 3: Install Dependencies

Run the following commands to install all required packages:

```bash
pip install langgraph langchain langchain-openai langchain-groq langchain-community langchain-tavily psycopg[binary] psycopg_pool python-dotenv tavily-python requests streamlit
pip install -U "psycopg[binary,pool]" langgraph-checkpoint-postgres
```

### Step 4: Install PostgreSQL

Download and install PostgreSQL for your operating system:
🔗 Download PostgreSQL

⚠️ **Important:** While installing PostgreSQL, remember:
* PostgreSQL Master Password
* Port Number (typically 5432 or 5433)

You will need them later while creating the database connection string.

### Step 5: Create Database

Open your PostgreSQL terminal (psql) or pgAdmin and run:

```sql
CREATE DATABASE langgraph_memory_demo;
```

### Step 6: Get Required API Keys

Obtain the necessary API credentials from the respective platforms:
* **Groq API Key:** console.groq.com
* **Tavily API Key:** tavily.com
* **AviationStack API Key:** aviationstack.com

### Step 7: Configure Environment Variables

Create a `.env` file in the root directory and add your keys:

```
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
AVIATIONSTACK_API_KEY=your_aviationstack_api_key
DATABASE_URL=postgresql://postgres:postgres@localhost:5433/langgraph_memory_demo
```

(Update `postgres:postgres` with your PostgreSQL username and password, and ensure the port matches your local setup).

### Step 8: Run the Application

**Option A: Test via Terminal (CLI Mode)**

```bash
python main.py
```

**Option B: Run Streamlit Web Application**

```bash
streamlit run frontend.py
```

---

## 💡 Usage Example

Test the multi-agent system with prompts such as:

> "Plan a complete 7 days Japan trip including flights, hotels, and sightseeing under 2 lakhs."

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to open a PR or issue on GitHub.

---

## 👤 Author

**Abhinav Choudhary**
GitHub: [@abhinavchoudhary2003](https://github.com/abhinavchoudhary2003)

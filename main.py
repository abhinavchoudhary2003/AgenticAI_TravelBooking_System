import os# 'os' -> Standard library. Used to read environment variables (like API keys)  that get loaded from the .env file, e.g. os.environ["GROQ_API_KEY"].

from typing import TypedDict, Annotated
# 'TypedDict' -> Lets us define the shape of our LangGraph "State" dictionary with fixed keys and types (e.g. messages: list[AnyMessage]).
# 'Annotated' -> Lets us attach metadata to a state field, most commonly used with LangGraph's reducer functions (like operator.add) to tell LangGraph HOW to merge/update that field across graph steps.

import operator
# 'operator' -> Standard library. Provides operator.add, which we pass into Annotated[] so LangGraph knows to APPEND new messages to the messages list instead of overwriting it on every node update.

# import psycopg # 'psycopg' (psycopg3) -> PostgreSQL database driver for Python. Required because we're using Postgres as the backend to store LangGraph checkpoints


from langgraph.graph import StateGraph, START, END
# 'langgraph' -> Core framework for building the agent as a graph of nodes
# StateGraph -> the graph builder class.
# START, END -> special constants marking the graph's entry and exit points.

from langgraph.checkpoint.postgres import PostgresSaver
# 'PostgresSaver' -> LangGraph's built-in checkpointer that saves graph state to a Postgres database. This is what gives the agent persistent memory
# (so conversations can resume across sessions/restarts). Needs psycopg under the hood to actually talk to Postgres.

from langchain_core.messages import (
    AnyMessage,
    HumanMessage,
    AIMessage,
    SystemMessage,
)
# 'langchain_core' -> Base message classes used to represent conversation turns in a structured way (who said what).
# AnyMessage   -> generic type covering any message class (used in typing).
# HumanMessage -> represents user input.
# AIMessage    -> represents the model's response.
# SystemMessage-> give instruction or behaviour rules to the model 

from langchain_groq import ChatGroq
# 'langchain-groq' -> LangChain's integration for Groq's LLM API. This is
# the actual chat model we're using to power the agent's reasoning
# (Groq is used here for its fast inference speed).

from tools.tavily_tool import tavily_search
# Local module -> Wraps the Tavily web search API as a LangChain-compatibletool, so the agent can search the internet for real-time info
# (e.g. current events, live prices) that the LLM doesn't know on its own.

from tools.flight_tool import search_flights
# Local module -> Custom tool (project-specific) that lets the agent search for flights, likely calling a flights/travel API. This is what makes the
# agent a "travel agent" rather than a generic chatbot.

from dotenv import load_dotenv
# 'python-dotenv' -> Loads environment variables from a .env file into
# os.environ, so secrets like GROQ_API_KEY, TAVILY_API_KEY, DB connection
# strings etc. don't need to be hardcoded in the source code.

load_dotenv() # Actually reads the .env file at runtime and populates os.environ with its key-value pairs, before any package below tries to use those keys.

DATABASE_URL = os.getenv("DATABASE_URL") # we need db to store our agents converstains

# Add LLM ModeL
llm = ChatGroq(
    model="openai/gpt-oss-120b"
)
#State is the shared information storage of our workflow. Agents can read information from the state and write their results back into it.
# TravelState is the shared memory of our workflow. Every node (agent) can read information from this state  and can also add or update information in the state. LangGraph passes this state from one node to the next.


class TravelState(TypedDict):
    messages: Annotated[list[AnyMessage], operator.add]# messages stores all the messages created during the workflow.It can contain messages from the user, AI agents, or other instructions.operator.add means new messages are added to the existing list instead of replacing the old messages.
    user_query: str# This stores the original request given by the user.# Other agents can read this value and use it to perform their tasks.
    flight_results: str# This stores the results produced by the flight agent.# The flight agent writes the results here, and the itinerary agent later reads them.
    hotel_results: str # This stores the results produced by the hotel agent. The hotel agent writes the results here, and the itinerary agent later reads them.
    itinerary: str# This stores the travel itinerary created by the itinerary agent. The final agent reads this information to create the final response.
    llm_calls: int # This keeps track of how many times our LLM is called. Each node increases this number when it performs its work.


# ── Flight agent ────────────────────────────────────────────────────────
# This agent reads the user's query and searches for flight information.
# It writes the flight results into the flight_results field.
# This agent directly calls search_flights() instead of calling an LLM.

def flight_agent(state: TravelState):

    # Get the user's original query from the shared state.
    query = state["user_query"]

    # Send the user's query to the flight search function.
    flight_data = search_flights(query)


    # Return the information that this agent wants to add/update in the state. LangGraph will merge this returned dictionary into the existing state.
    return {
        "flight_results": flight_data,

        # Add a message to the message history to show that
        # the flight information has been fetched.
        "messages": [
            AIMessage(content="Flight results fetched")
        ],

        # Increase the counter by 1.
        # Note: this function does not actually call an LLM,
        # so this counter is technically counting this node's call,
        # not only actual LLM calls.
        "llm_calls": state.get("llm_calls", 0) + 1
    }


# ── Hotel agent ─────────────────────────────────────────────────────────
# This agent reads the user's query and searches for hotel information.
# It writes the hotel results into the hotel_results field.
# This agent also uses a tool/function instead of directly calling the LLM.

def hotel_agent(state: TravelState):

    # Get the user's query and create a search query for hotels.
    query = f"Best hotels for {state['user_query']}"

    # Search the internet using Tavily.
    hotel_results = tavily_search(query)


    # Return the hotel results and other information that needs to be added to the shared state.
    return {
        "hotel_results": hotel_results,

        # Add a message to the message history
        # showing that hotel information was fetched.
        "messages": [
            AIMessage(content="Hotel information fetched")
        ],

        # Increase the counter by 1.
        "llm_calls": state.get("llm_calls", 0) + 1
    }


# ── Itinerary agent ─────────────────────────────────────────────────────
# This agent reads the user's query, flight results, and hotel results.
# It then uses the LLM to create a complete travel itinerary.
# The generated itinerary is stored in the itinerary field.

def itinerary_agent(state: TravelState):

    # Create a prompt containing all the information that the LLM needs to create the travel itinerary.
    prompt = f"""
    Create a travel itinerary.
    User Query:
    {state['user_query']}

    Flight Results:
    {state['flight_results']}

    Hotel Results:
    {state['hotel_results']}
    """
    # Send the instructions and travel information to the LLM. The LLM will use this information to create the itinerary.
    response = llm.invoke([
        SystemMessage(content="You are an expert travel planner"),
        HumanMessage(content=prompt)
    ])


    # Save the LLM's response as the itinerary. Also add the response to the message history.
    return {
        "itinerary": response.content,

        # Store the complete AI response in the messages list.
        "messages": [response],

        # Increase the LLM call counter by 1.
        "llm_calls": state.get("llm_calls", 0) + 1
    }


# ── Final response agent ────────────────────────────────────────────────
# This agent reads the flight results, hotel results, and itinerary. It uses the LLM to create the final response that will be shown to the user.

def final_agent(state: TravelState):

    # Create a prompt containing all the information
    # that should be included in the final response.
    final_prompt = f"""
    Generate final travel response.

    Flights:
    {state['flight_results']}

    Hotels:
    {state['hotel_results']}

    Itinerary:
    {state['itinerary']}
    """


    # Send the final travel information to the LLM.
    # The LLM uses this information to create the final user-facing response.
    response = llm.invoke([
        HumanMessage(content=final_prompt)
    ])


    # Add the final LLM response to the message history.
    # This node doesn't create a new field such as final_response.
    return {
        "messages": [response],

        # Increase the LLM call counter by 1.
        "llm_calls": state.get("llm_calls", 0) + 1
    }


# ── Build the graph ─
# StateGraph is used to build our workflow.
# It connects all our nodes and controls the order in which they run.
graph = StateGraph(TravelState)


# Add each agent/function to the graph.
# The name on the left is the name we give to the node.
graph.add_node("flight_agent", flight_agent)
graph.add_node("hotel_agent", hotel_agent)
graph.add_node("itinerary_agent", itinerary_agent)
graph.add_node("final_agent", final_agent)


# Connect the nodes and decide the order in which they should run.
# The workflow will run like this:
#
# START
#   ↓
# flight_agent
#   ↓
# hotel_agent
#   ↓
# itinerary_agent
#   ↓
# final_agent
#   ↓
# END
#
# Flight and hotel agents both only need the user_query.
# They don't actually depend on each other's results.
# They are running one after another here because we connected them
# in a sequential order.

graph.add_edge(START, "flight_agent")
graph.add_edge("flight_agent", "hotel_agent")
graph.add_edge("hotel_agent", "itinerary_agent")
graph.add_edge("itinerary_agent", "final_agent")
graph.add_edge("final_agent", END)


#Persistence
# A checkpointer allows LangGraph to save the state of our workflow.
# Here, we are using PostgreSQL to store that saved state.
# This allows us to continue a conversation later instead of losing
# the state when the program stops.


# Open a connection to our PostgreSQL database.
# _conn = psycopg.connect(DATABASE_URL)
# _conn = psycopg.connect(DATABASE_URL, autocommit=True)

# # Create a LangGraph checkpointer using the PostgreSQL connection.
# checkpointer = PostgresSaver(_conn)

# # Create the required checkpoint tables in the database if they don't already exist.
# checkpointer.setup()


# Compile the graph so it becomes a runnable application. The checkpointer is connected to the graph so LangGraph can save and restore the state of each conversation.
app = graph.compile()

# This block runs only when we directly run this Python file, not when this file is imported into another file. this is just for testing the agents 
# if __name__ == "__main__":
#     config = {
#         "configurable": {
#             "thread_id": "user_name"# thread_id gives each conversation a unique identity, which allows LangGraph's checkpointer to save and retrieve its state.

#         }
#     }
#     user_input = input("Enter travel request: ") # input() takes the user's travel request from the terminal and stores that request in the user_input variable.

#     result = app.invoke(
#         {
#             "messages": [
#                 HumanMessage(content=user_input)
#             ],
#             "user_query": user_input,
#             "flight_results": "",
#             "hotel_results": "",
#             "itinerary": "",
#             "llm_calls": 0
#         },
#         config=config
#     )
#     # app.invoke() starts the LangGraph workflow by sending the user's request and the initial TravelState to the graph.

#     print("\nFINAL RESPONSE:\n")# This prints a heading so we can easily identify where the final workflow response starts.

#     for msg in result["messages"]:# The messages list contains the messages created during the workflow, so this loop reads them one by one.

#         print(msg.content) # .content contains the actual text of the message, so print it to show the message on the screen.


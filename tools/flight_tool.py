# Example free API usage
# - AviationStack

# Create an API key from the AviationStack website.
# https://aviationstack.com/
# Install the requests library using: pip install requests

import os
# os is a built-in Python module.
# We use it to read the AviationStack API key from the environment,
# instead of writing the secret API key directly in our code.

import requests
# requests is a Python library used to send HTTP requests.
# We use it here to send a request to the AviationStack API
# and receive flight information from it.

from dotenv import load_dotenv
# load_dotenv comes from the python-dotenv package.
# It helps us load the values stored in our .env file
# so that our Python program can use them.

load_dotenv()
# This loads the values from the .env file into the environment.
# After this, we can use os.getenv() to read the API key.

API_KEY = os.getenv("AVIATIONSTACK_API_KEY")
# Get the value of AVIATIONSTACK_API_KEY from the environment.
# The API key is stored in the .env file instead of directly in our code.
# If the key is not found, os.getenv() returns None.


def search_flights(query):
    # This function searches for flight information using AviationStack.
    # Our LangGraph agent can call this function when it needs flight data.
    # The query is received by the function, but it is not being used
    # in the current version of this code.

    url = "http://api.aviationstack.com/v1/flights"
    # This is the AviationStack API endpoint.
    # We send our request to this URL to get flight information.

    params = {
        "access_key": API_KEY,
        "limit": 5
    }
    # These are the parameters we send along with our API request.
    # access_key tells AviationStack which API key we are using.
    # limit=5 tells the API that we only want 5 flight results.

    response = requests.get(url, params=params)
    # Send a GET request to the AviationStack API.
    # The API receives our URL and parameters and sends a response back.

    data = response.json()
    # Convert the API response from JSON into a Python dictionary.
    # This makes it easier for us to access the flight information.

    flights = []
    # Create an empty list to store the flight information.
    # We will format each flight into a simple readable text block.

    if "data" in data:
        # Check whether the response contains a "data" field.
        # This field normally contains the list of flights.
        # We check first so our code doesn't try to access missing data.

        for flight in data["data"][:5]:
            # Go through the flight results one by one.
            # [:5] makes sure we only process the first 5 flights.

            airline = flight.get("airline", {}).get("name", "Unknown")
            # Get the airline name from the flight information.
            # The airline information is inside a nested "airline" object.
            # If the information is missing, we use "Unknown" instead.

            departure = flight.get("departure", {}).get("airport", "Unknown")
            # Get the departure airport from the nested "departure" object.
            # If the airport information is missing, use "Unknown".

            arrival = flight.get("arrival", {}).get("airport", "Unknown")
            # Get the arrival airport from the nested "arrival" object.
            # If the airport information is missing, use "Unknown".

            status = flight.get("flight_status", "Unknown")
            # Get the current status of the flight.
            # If the status is not available, use "Unknown".

            flights.append(f"""
Airline: {airline}
Departure: {departure}
Arrival: {arrival}
Status: {status}
""")
            # Create a readable text block containing the flight details.
            # Then add that text block to our flights list.

    return "\n".join(flights)
    # Join all the flight results together into one string.
    # "\n" puts each flight result on a separate line.
    # Finally, return the formatted flight information.
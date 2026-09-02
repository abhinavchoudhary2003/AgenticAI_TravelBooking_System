from tavily import TavilyClient



import os 
# os is a built-in Python module.
# We use it to read the value of the Tavily API key from our environment variables.


from dotenv import load_dotenv 
# load_dotenv helps us load the values stored in our .env file in our program .
# Our .env file contains the Tavily API key, so we don't have to write the secret API key directly in our Python code.

load_dotenv() # `load_dotenv()` loads the values from the `.env` file into the Python program, so we don't have to hardcode them directly in our code.
# This loads the variables from the .env file into the environment.
# After this, we can use os.getenv() to access our API key.

client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY") # 
)
# Create a Tavily client and give it our API key.
# os.getenv("TAVILY_API_KEY") looks for the API key in our environment.
# This client will be used to communicate with Tavily and perform searches.

# os.getenv() doesn't automatically look inside the .env file to read a specific value.
# So, load_dotenv() first loads the values from the .env file and makes them available to our Python program.
# Then, os.getenv("TAVILY_API_KEY") gets the specific value we want from the environment.


def tavily_search(query):
    # This function receives a search query and sends it to Tavily.
    # Our LangGraph agent can call this function when it needs
    # up-to-date information from the internet.

    response = client.search(
        query=query,
        max_results=5
    )
    # Send the query to Tavily and ask for up to 5 search results.
    # Tavily gives the search results back and stores them in 'response'.


    results = []
    # Create an empty list where we will store our formatted results.
    # We do this because Tavily's original response contains more data
    # than we need, so we will create a simpler version.


    for i, r in enumerate(response["results"], 1):
        # Go through each result one at a time.
        # 'i' is the result number (1, 2, 3, etc.).
        # 'r' contains the information about the current search result.


        title   = r.get("title", "Unknown")
        # Get the title of the webpage from the current result.
        # If a title is not available, use "Unknown" instead.


        url     = r.get("url", "")
        # Get the URL of the webpage.
        # If Tavily doesn't provide a URL, use an empty string instead.


        snippet = r.get("content", "").strip()
        # Get the content or text that Tavily returned for this webpage.
        # strip() removes unnecessary spaces from the beginning and end.


        # Keep only the first 300 characters to avoid sending too much text.
        if len(snippet) > 300:
            snippet = snippet[:300].rsplit(" ", 1)[0] + "..."
        # If the snippet has more than 300 characters, make it shorter.
        # rsplit() makes sure we don't cut the text in the middle of a word.
        # Finally, "..." shows that some content was removed.


        results.append(f"{i}. **{title}**\n   {url}\n   {snippet}")
        # Add the number, title, URL, and snippet to our results list.
        # This gives us a simple and readable format for each search result.


    return "\n\n".join(results)
    # Join all the results together into one string.
    # "\n\n" puts a blank line between each search result.
    # The final string is what our LangGraph agent will receive.




    
    
    # test it
#################################
# response = client.search(
    # query="Best hotels in Dubai"
# )

# print(response)

####################################

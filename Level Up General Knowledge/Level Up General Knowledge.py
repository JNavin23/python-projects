import wolframalpha

# IMPORTANT: To use this tool, replace "YOUR_APP_ID_HERE" with your actual Wolfram Alpha App ID.
# Get one for free at: developer.wolframalpha.com

app_id = "YOUR_APP_ID_HERE"

client = wolframalpha.Client(app_id)


print("Welcome to 'Level Up General Knowledge'!")
print("\n")
print("Type 'exit' or 'quit' to end the session.")


while True:
    query = input("Ask your question: ")
    if query.lower() in ["exit", "quit"]:
        print("Exiting. Goodbye!")
        break
    try:
        result = client.query(query)
        answer = next(result.results).text
        print("Answer:", answer)
    except:
        print("No answer found.")
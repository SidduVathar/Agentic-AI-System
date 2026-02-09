from openai import OpenAI

# 1. Initialize the client to point at your LOCAL PROXY
client = OpenAI(
    api_key="master_key",  # Must match 'master_key' in your config.yaml
    base_url="http://localhost:4000" # The address where your Docker container is listening
)


print("--- Sending request to Local Proxy ---")
# 2. Call the 'model_name' you defined in your yaml (e.g., 'gemini')
completion = client.chat.completions.create(
model="#Modle Name",
messages=[
    {
        "role": "user",
        "content": "Describe about the capital city of Germany."
    }
],
    )
print(completion.choices[0].message)

# 3. Print the results
# print(f"Status: Success!")
# print(f"Response: {response.choices[0].message.content}")
# print(f"Usage: {response.usage.total_tokens} tokens")


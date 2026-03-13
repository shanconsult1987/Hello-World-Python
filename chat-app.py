import os
from dotenv import load_dotenv

from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

def main():

```
os.system('cls' if os.name == 'nt' else 'clear')

try:

    # Load environment variables
    load_dotenv()

    project_endpoint = os.getenv("PROJECT_ENDPOINT")
    model_deployment = os.getenv("MODEL_DEPLOYMENT")

    # Initialize Azure AI Project client
    project_client = AIProjectClient(
        endpoint=project_endpoint,
        credential=DefaultAzureCredential()
    )

    # Get OpenAI client from project
    openai_client = project_client.get_openai_client()

    # Conversation history
    messages = [
        {"role": "system", "content": "You are a helpful AI assistant."}
    ]

    print("Azure AI Foundry Chat App")
    print("Type 'quit' to exit\n")

    while True:

        user_input = input("You: ")

        if user_input.lower() == "quit":
            break

        if not user_input.strip():
            continue

        messages.append({"role": "user", "content": user_input})

        response = openai_client.chat.completions.create(
            model=model_deployment,
            messages=messages
        )

        reply = response.choices[0].message.content

        print("\nAssistant:", reply, "\n")

        messages.append({"role": "assistant", "content": reply})

except Exception as ex:
    print("Error:", ex)
```

if **name** == "**main**":
main()

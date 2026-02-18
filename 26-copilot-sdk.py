# GitHub Copilot SDK
# You can use the Copilot SDK to build a command-line assistant. You'll start with the basics, add streaming responses, then add custom tools - giving Copilot the ability to call your code.

# Step 1
# Make sure GitHub Copilot CLI installed and authenticated https://docs.github.com/en/copilot/how-tos/set-up/install-copilot-cli
# Install the relevant GitHub Copilot SDK (e.g. for Python: pip install github-copilot-sdk)

# Step 2
# Run this script in the terminal: py 26-copilot-sdk.py
# You should see a response from the Copilot assistant.

# Learn more: https://github.com/github/copilot-sdk/blob/main/docs/getting-started.md


import asyncio
from copilot import CopilotClient


async def main():
    client = CopilotClient()
    await client.start()

    session = await client.create_session({
        "system_message": "You are a helpful assistant that provides information about Microsoft Azure services.",
        "model": "gpt-4.1",
        "mcp_servers": {
            "azure-docs": {
                "type": "http",
                "url": "https://learn.microsoft.com/api/mcp",
                "tools": ["*"],
            }
        }
    })
    response = await session.send_and_wait({"prompt": 
        "Create a simple python calculator and save the file as calculator.py."})

    print(f"Response: {response.data.content}")
    print("***")
    print(f"Raw response: {response.to_dict()}")

    await client.stop()

asyncio.run(main())

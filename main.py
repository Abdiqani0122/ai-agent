from agent.agent import Agent

agent = Agent()

print("Talk to the agent (type 'exit' to quit)\n")

while True:
    text = input("You: ")

    if text.lower() == "exit":
        print("Goodbye")
        break

    result = agent.act(text)
    print("\nAgent: ")
    print(result)
    print("-" * 40)

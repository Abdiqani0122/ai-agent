from agent.agent import Agent

agent = Agent()

text = input("Say something: ")

result = agent.act(text)

print("\nAgent response:")
print(result)
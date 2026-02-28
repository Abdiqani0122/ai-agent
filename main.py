from agent.agent import Agent

agent = Agent()

task = input("What do you want me to do? ")
text = input("Enter text: ")

result = agent.act(task, text)

print("\nAgent response:")
print(result)
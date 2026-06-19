from crewai import Agent, Task, Crew, LLM

llm = LLM(
    model="ollama/qwen3:8b",
    base_url="http://localhost:11434"
)

developer = Agent(
    role="Python Developer",
    goal="Write Python code",
    backstory="Senior Python developer.",
    llm=llm,
    verbose=True
)

task = Task(
    description="Write a Python program that prints Hello World.",
    expected_output="Python code",
    agent=developer,
)

crew = Crew(
    agents=[developer],
    tasks=[task],
    verbose=True,
)

result = crew.kickoff()

print(result)
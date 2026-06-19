from crewai import Agent

developer = Agent(
    role="Senior Python Developer",
    goal="Write clean, production-ready Python code.",
    backstory=(
        "You are a senior software engineer specialized "
        "in AI automation and backend systems."
    ),
    verbose=True
)
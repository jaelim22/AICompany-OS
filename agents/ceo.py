from crewai import Agent

ceo = Agent(
    role="CEO",
    goal="Manage all AI workers and assign tasks efficiently.",
    backstory=(
        "You are the CEO of AICompany. "
        "You coordinate developers, researchers and automation agents."
    ),
    verbose=True
)
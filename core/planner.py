from core.engine import engine


def create_plan(task):
    prompt = f"""
다음 작업을 단계별 계획으로 작성해라.

작업:
{task}
"""

    return engine.run("Planner", prompt)
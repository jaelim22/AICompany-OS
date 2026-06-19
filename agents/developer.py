from core.engine import engine


def develop(plan):
    prompt = f"""
다음 계획을 코드로 구현해라.

{plan}
"""

    return engine.run("Developer", prompt)
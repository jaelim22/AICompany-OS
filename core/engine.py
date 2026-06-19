from llm.ollama_client import ask_ollama


class AIEngine:
    def __init__(self):
        self.model = "qwen2.5-coder:7b"

    def run(self, role, prompt):
        system_prompt = f"""
너는 AICompany의 {role}이다.

역할에 맞게 답변해라.
"""

        return ask_ollama(system_prompt + "\n\n" + prompt)


engine = AIEngine()
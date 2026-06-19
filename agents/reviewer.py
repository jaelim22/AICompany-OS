from llm.ollama_client import ask_ollama

def review(code):
    prompt = f"""
너는 시니어 코드 리뷰어다.

아래 코드를 검토하고

1. 버그
2. 개선점
3. 보안 문제

를 알려줘.

{code}
"""

    return ask_ollama(prompt)
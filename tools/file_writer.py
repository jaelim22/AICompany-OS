from pathlib import Path

def save_code(project_name, code):
    project = Path(project_name)

    project.mkdir(exist_ok=True)

    file = project / "main.py"

    file.write_text(code, encoding="utf-8")

    print(f"✅ {file} 저장 완료")
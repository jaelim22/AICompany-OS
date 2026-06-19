from pathlib import Path

def create_project(project_name):
    base = Path(project_name)

    base.mkdir(exist_ok=True)

    (base / "README.md").write_text(f"# {project_name}\n")
    (base / "requirements.txt").write_text("")
    (base / "main.py").write_text('print("Hello from AICompany")')

    print(f"✅ {project_name} 프로젝트 생성 완료!")
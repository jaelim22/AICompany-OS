from core.planner import create_plan
from agents.developer import develop
from agents.reviewer import review
from tools.project_builder import build_project

task = input("작업 입력 : ")

print("\n[1] 계획 생성")
plan = create_plan(task)
print(plan)

print("\n[2] 코드 생성")
code = develop(plan)

print("\n[3] 코드 리뷰")
review_result = review(code)
print(review_result)

print("\n[4] 프로젝트 생성")
build_project("output_project")

print("\n✅ AICompany 작업 완료")
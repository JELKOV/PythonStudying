# 사용자 이름을 입력받아 특정 메시지를 출력하는 함수
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")

greet_with_name("Jack Bauer")

# 이름과 위치를 입력받아 인사 메시지를 출력하는 함수
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with("jaeho", "gangnam")

# 키워드 인자를 사용하여 순서와 상관없이 호출
greet_with(location="gangnam", name="jaeho")
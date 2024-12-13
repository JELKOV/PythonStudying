# Functions with input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet_with_name("Jack Bauer")


def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with("jaeho", "gangnam")

# 키워드 인장
greet_with(location="gangnam", name="jaeho")
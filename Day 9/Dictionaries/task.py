# 딕셔너리 정의 및 사용 예제
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# 특정 키 값 출력
print(programming_dictionary["Bug"])

# 딕셔너리에 새 키-값 쌍 추가
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

# 빈 딕셔너리 정의
empty_dictionary = {}

# 초기화 예시 (주석 처리됨)
# programming_dictionary = empty_dictionary
# print(programming_dictionary)

# 기존 키의 값 수정
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)

# 딕셔너리 반복 처리
for thing in programming_dictionary:
    print(thing)  # 키 출력
    print(programming_dictionary[thing])  # 해당 키의 값 출력
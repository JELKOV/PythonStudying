def format_name(f_name, l_name):
    # 이름과 성을 입력받아 각 첫 글자를 대문자로 변환한 뒤 반환하는 함수
    return f"{f_name.title()} {l_name.title()}"

# "ahn jaeho"를 대문자로 포맷팅하여 변수에 저장
formatting_string = format_name("ahn", "jaeho")

# 포맷팅된 문자열 출력
print(formatting_string)

# 문자열을 두 번 반복하여 반환하는 함수
def function_1(text):
    return text + text

# 문자열의 첫 글자를 대문자로 변환하여 반환하는 함수
def functino_2(text):
    return text.title()

# "HELLO"를 두 번 반복한 결과를 출력
output = function_1("HELLO")

# "HELLO"를 두 번 반복하고 첫 글자를 대문자로 변환한 결과를 출력
output1 = functino_2(function_1("HELLO"))

print(output)
print(output1)
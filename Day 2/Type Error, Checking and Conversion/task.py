# len 함수는 문자열의 길이를 반환
len("Hello")

# Type Error 예시
# len(12345)  # 숫자는 길이를 구할 수 없으므로 TypeError 발생
# 문자열, 바이트, 튜플, 딕셔너리, 세트와 같은 컬렉션만 len 함수 사용 가능

# Type Checking (자료형 확인)
print(type("Hello"))  # <class 'str'>: 문자열
print(type(123))      # <class 'int'>: 정수
print(type(True))     # <class 'bool'>: 불리언
print(type(1.2313))   # <class 'float'>: 실수

# Type Conversion (자료형 변환)
print(int("123") + int("456"))  # 문자열을 정수로 변환 후 더함 (579)

# 사용자 입력 및 문자열 길이 계산
name_of_the_user = input("Enter your name")  # 사용자 입력 받기
length_of_the_name = len(name_of_the_user)  # 입력된 문자열의 길이 구하기
print("Number of letters in your name: " + str(length_of_the_name))  # 결과 출력
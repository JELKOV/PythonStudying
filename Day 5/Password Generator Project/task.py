# 랜덤 비밀번호 생성기
import random

# 비밀번호에 사용할 문자, 숫자, 기호 리스트 정의
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# 사용자 입력: 비밀번호에 포함할 문자, 숫자, 기호의 개수
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# # 쉬운 버전 (주석 처리됨)
# password = ""
# for char in range(0, nr_letters):
#     password += random.choice(letters)
#
# for sym in range(0, nr_symbols):
#     password += random.choice(symbols)
#
# for num in range(0, nr_numbers):
#     password += random.choice(numbers)
#
# print(password)

# 어려운 버전
passwordHard_list = []

# 비밀번호에 사용할 랜덤 문자 추가
for char in range(0, nr_letters):
    passwordHard_list.append(random.choice(letters))

# 비밀번호에 사용할 랜덤 기호 추가
for sym in range(0, nr_symbols):
    passwordHard_list.append(random.choice(symbols))

# 비밀번호에 사용할 랜덤 숫자 추가
for num in range(0, nr_numbers):
    passwordHard_list.append(random.choice(numbers))

# 비밀번호 요소를 무작위로 섞기
random.shuffle(passwordHard_list)
print(passwordHard_list)

# 리스트를 문자열로 변환하여 최종 비밀번호 출력
password = ""
for char in passwordHard_list:
    password += char

print(f"Your password is: {password}")
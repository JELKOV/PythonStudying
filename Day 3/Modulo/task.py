# 짝수인지 홀수인지 확인하는 프로그램
number_to_check = int(input("What is the number you want to check"))  # 사용자에게 숫자 입력 받기

print(number_to_check % 2)  # 나머지를 출력하여 확인

# 나머지가 0인지 확인 (짝수 조건)
if number_to_check % 2 == 0:
    print("EVEN")  # 짝수면 출력
else:
    print("ODD")  # 홀수면 출력

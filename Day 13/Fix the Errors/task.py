while True:  # 입력이 올바를 때까지 반복
    try:
        age = int(input("How old are you? "))  # 나이 입력 받기
        break  # 올바른 값이 입력되면 반복 종료
    except ValueError:
        print("잘못된 입력입니다. 숫자로 입력해주세요.")  # 잘못된 입력 처리

# 운전 가능 여부 확인
if age > 18:
    print(f"You can drive at age {age}.")
else:
    print(f"You cannot drive at age {age}.")

print("Welcome to Python Pizza Deliveries!")

# 사용자 입력 받기
size = input("What size pizza do you want? S, M or L: ")  # 피자 사이즈
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")  # 페퍼로니 추가 여부
extra_cheese = input("Do you want extra cheese? Y or N: ")  # 추가 치즈 여부

bill = 0  # 초기 요금 설정

# 피자 사이즈에 따라 요금 설정
if size == "S":
    bill += 15  # Small 피자 요금
elif size == "M":
    bill += 20  # Medium 피자 요금
elif size == "L":
    bill += 25  # Large 피자 요금
else:
    print("wrong")  # 잘못된 입력 처리

# 페퍼로니 추가 요금 계산
if pepperoni == "Y":
    if size == "S":
        bill += 2  # Small 사이즈는 $2 추가
    else:
        bill += 3  # Medium, Large 사이즈는 $3 추가

# 추가 치즈 요금 계산
if extra_cheese == "Y":
    bill += 1  # 추가 치즈는 $1 추가

print(f"Your final bill is: ${bill}.")  # 최종 요금 출력

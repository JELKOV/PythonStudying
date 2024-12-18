print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))  # 사용자 키 입력 받기

# 초기 요금 설정
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))  # 나이 입력
    if age <= 12:
        bill = 5  # 어린이 요금
        print("Please pay $5.")
    elif age <= 18:
        bill = 7  # 청소년 요금
        print("Please pay $7.")
    else:
        bill = 12  # 성인 요금
        print("Please pay $12.")

    # 사진 추가 여부 확인
    wants_photo = input("Do you wanna photo ticket? Y or N: ").upper()
    if wants_photo == "Y":
        bill += 3  # 사진 추가 비용 $3
    print(f"Your final bill is ${bill}")  # 최종 요금 출력
else:
    print("Sorry you have to grow taller before you can ride.")

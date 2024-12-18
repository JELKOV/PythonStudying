print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))  # 사용자 키 입력

bill = 0  # 초기 요금 설정

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))  # 나이 입력
    if age < 12:
        bill = 5
        print("Child tickets are $5.")  # 어린이 요금
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")  # 청소년 요금
    elif 45 <= age <= 55:
        bill = 0  # 중년 무료 티켓
        print("Free tickets")
    else:
        bill = 12
        print("Adult tickets are $12.")  # 성인 요금

    wants_photo = input("Do you want a photo taken? Y or N. ").upper()
    if wants_photo == "Y":
        bill += 3  # 사진 추가 비용

    print(f"Your final bill is ${bill}")  # 최종 요금 출력
else:
    print("Sorry, you have to grow taller before you can ride.")  # 키 부족

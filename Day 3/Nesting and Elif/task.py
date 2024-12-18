print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))  # 사용자 키 입력 받기

# 키가 120cm 이상인지 확인
if height >= 120:
    print("You can ride the rollercoaster")  # 탑승 가능
    age = int(input("What is your age? "))  # 사용자 나이 입력 받기
    if age <= 12:
        print("5불 내세요")  # 12세 이하 요금
    elif age <= 18:
        print("7불 내세요")  # 18세 이하 요금
    else:
        print("12불 내세요")  # 성인 요금
else:
    print("Sorry you have to grow taller before you can ride.")  # 키 부족

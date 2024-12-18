# 롤러코스터 탑승 여부 확인
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))  # 사용자에게 키 입력 받기

# 키가 120cm 이상인지 확인
if height >= 120:
    print("롤러 코스터 가능")  # 키가 기준 이상이면 출력
else:
    print("못타요")  # 키가 부족하면 출력

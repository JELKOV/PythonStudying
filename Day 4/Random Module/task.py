import random  # 랜덤 라이브러리 불러오기
import my_module  # 사용자 정의 모듈 가져오기

# 1~10 사이의 랜덤 정수 생성
random_integer = random.randint(1, 10)
print(random_integer)

# my_module에서 favorite number 출력
print(my_module.my_favourite_number)

# 0과 1 사이의 랜덤 소수 생성 후 10을 곱해서 0~10 범위의 소수 만들기
random_number_0_to_1 = random.random() * 10
print(random_number_0_to_1)

# 1~10 사이의 랜덤 소수 생성 (uniform 사용)
random_float = random.uniform(1, 10)
print(random_float)

# 0 또는 1을 랜덤으로 생성하여 동전 던지기 구현
random_head_or_tails = random.randint(0, 1)
if random_head_or_tails == 0:
    print("Head")  # 결과가 0이면 앞면 출력
else:
    print("Tails")  # 결과가 1이면 뒷면 출력

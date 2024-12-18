import random  # 랜덤 라이브러리 불러오기

# 친구 이름 리스트 생성
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# 예시 출력: Bob 출력 (인덱스 1번 직접 출력)
print("Bob")

# 랜덤하게 리스트에서 친구 이름 선택 (choice 함수 사용)
print(random.choice(friends))

# 랜덤 인덱스 생성 및 해당 친구 이름 출력
random_index = random.randint(0, 4)  # 인덱스 범위: 0~4
print(friends[random_index])

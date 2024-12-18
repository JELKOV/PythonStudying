# 전역 변수 `enemies`를 선언하고 초기값 1로 설정
enemies = 1

# 로컬 스코프 예제: 함수 내부에서 선언된 변수는 함수 외부에서 접근할 수 없음
def increase_enemies():
    enemies = 2  # 함수 내부에서 로컬 변수로 `enemies` 선언
    print(f"enemies inside function: {enemies}")  # 함수 내부에서만 사용 가능

# 함수 호출
increase_enemies()

# 전역 변수 출력 (함수 내부의 로컬 변수와는 별개)
print(f"enemies outside function: {enemies}")

# 전역 변수 예제
player_health = 10  # 전역 변수 선언

def game():
    def drink_potion():
        potion_strength = 2  # 로컬 변수
        print(potion_strength)  # 로컬 변수 출력
        print(player_health)  # 전역 변수 출력

    drink_potion()  # 내부 함수 호출

# 전역 변수 출력
print(player_health)
# 전역 변수 `enemies`를 선언하고 초기값 1로 설정
enemies = 1


# 전역 변수 `enemies`를 수정하는 함수
def increase_enemies():
    global enemies  # 함수 내부에서 전역 변수 `enemies`를 사용하도록 선언
    enemies += 1  # 전역 변수 `enemies`의 값을 1 증가
    print(f"enemies inside function: {enemies}")  # 함수 내부에서 `enemies` 값을 출력


# `increase_enemies` 함수를 호출하여 전역 변수 `enemies` 값을 수정
increase_enemies()

# 함수 호출 이후 전역 변수 `enemies`의 값을 출력
print(f"enemies outside function: {enemies}")


# 전역 변수를 직접 수정하지 않고, 인자를 이용해 값을 변경하는 함수
def increases_enemies(enemy):
    # 함수 내부에서 전역 변수 `enemies`의 현재 값을 출력 (수정은 하지 않음)
    print(f"2enemies inside function: {enemies}")
    return enemy + 1  # 함수의 인자 `enemy`에 1을 더한 값을 반환


# `increases_enemies` 함수 호출로 반환된 값을 전역 변수 `enemies`에 다시 할당
enemies = increases_enemies(enemies)

# `increases_enemies` 함수 호출 후 전역 변수 `enemies`의 최종 값을 출력
print(f"2enemies outside function: {enemies}")

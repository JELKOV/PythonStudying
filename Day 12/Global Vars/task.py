# 전역 변수 수정 예제
def increase_enemies():
    global enemies  # 함수 내부에서 전역 변수 사용 선언
    enemies += 1  # 전역 변수 수정
    print(f"enemies inside function: {enemies}")

# 함수 호출
increase_enemies()

# 함수 호출 이후 전역 변수 출력
print(f"enemies outside function: {enemies}")

# 전역 변수를 수정하지 않고 인자로 전달하여 값 변경
def increases_enemies(enemy):
    print(f"2enemies inside function: {enemies}")
    return enemy + 1  # 인자 값을 증가시켜 반환

# 함수 호출로 반환된 값을 전역 변수에 저장
enemies = increases_enemies(enemies)

# 최종 전역 변수 출력
print(f"2enemies outside function: {enemies}")
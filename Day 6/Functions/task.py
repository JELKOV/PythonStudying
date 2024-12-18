# 함수 정의: my_function
def my_function():
    # "Hello" 출력
    print("Hello")
    # "Bye" 출력
    print("Bye")

# my_function 호출
my_function()

# Reeborg's World 문제 풀이 코드

# # 오른쪽으로 회전하는 동작 정의
# def turn_right():
#     # 왼쪽으로 3번 회전하면 오른쪽 회전과 동일
#     turn_left()
#     turn_left()
#     turn_left()
#
# # 장애물(벽)을 점프하는 동작 정의
# def jump():
#     count = 0  # 높이를 기록할 변수 초기화
#     turn_left()  # 왼쪽으로 회전
#     # 벽이 오른쪽에 있는 동안 계속 앞으로 이동
#     while wall_on_right():
#         move()
#         count += 1  # 이동한 칸수 증가
#     turn_right()  # 오른쪽으로 회전
#     move()  # 한 칸 앞으로 이동
#     turn_right()  # 다시 오른쪽으로 회전
#     # 벽 높이만큼 내려가기
#     for _ in range(count):
#         move()
#     turn_left()  # 왼쪽으로 회전하여 원래 방향으로 복귀
#
# # 목표 지점에 도달할 때까지 반복
# while not at_goal():
#     # 앞에 벽이 있으면 점프
#     if wall_in_front():
#         jump()
#     # 앞이 비어 있으면 이동
#     elif front_is_clear():
#         move()

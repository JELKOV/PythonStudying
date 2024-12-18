# game_level = 3
# enemies= ["Skeleton", "Zombie", "Alien"]
#
# if game_level < 5:
#     new_enemy =enemies[0]
#
# print(new_enemy)

# 조건문과 전역 변수 사용 예제
game_level = 3  # 게임 레벨 설정
enemies = ["Skeleton", "Zombie", "Alien"]  # 적 리스트 정의

def create_enemy():
    # 로컬 변수로 적 생성
    if game_level < 5:
        new_enemy = enemies[0]  # 게임 레벨이 5 미만일 경우 첫 번째 적 선택
        print(new_enemy)

# 함수 호출
create_enemy()
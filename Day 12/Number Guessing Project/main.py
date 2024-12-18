# 우선 게임을 시작할지를 묻는다.

# 게임을 시작하고 Easy (10attempt) & Hard(5attempt) 버전을 선택할수 있게 만든다.

# 그리고 임의의 숫자를 1~100까지 중에 정한다. 보여주진 않는다.

# 그리고 input을 받아서 그값에 따라 up down을 알려준다.

# 횟수 안에 성공하면 성공, 아니면 실패를 알려준다.


import random
from art import logo

print("\n===== 업다운 게임 =====")
def start_game():

    # 게임 시작 여부를 묻는다
    play_game = input("게임을 시작하시겠습니까? (y/n): ").lower()
    if play_game != 'y':
        print("게임을 종료합니다.")
        return
    print(logo)
    # 난이도를 선택한다
    difficulty = input("난이도를 선택하세요: Easy(10번) 또는 Hard(5번): ").lower()
    attempts = 10 if difficulty == 'easy' else 5
    print(f"{attempts}번의 기회가 주어집니다!")

    # 임의의 숫자를 정한다
    target = random.randint(1, 100)

    # 게임 시작
    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"숫자를 입력하세요 (1~100): "))
            if guess < 1 or guess > 100:
                print("1에서 100 사이의 숫자를 입력해주세요.")
                continue

            if guess < target:
                print("UP!")
            elif guess > target:
                print("DOWN!")
            else:
                print(f"축하합니다! 정답입니다. {attempt}번 만에 맞추셨습니다!")
                break
        except ValueError:
            print("유효한 숫자를 입력해주세요.")
            continue

        if attempt == attempts:
            print(f"기회를 모두 사용하셨습니다. 실패! 정답은 {target}이었습니다.")


# 게임 실행
start_game()

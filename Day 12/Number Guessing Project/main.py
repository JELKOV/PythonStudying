# ===== 업다운 게임 =====
import random
from art import logo

print("\n===== 업다운 게임 =====")

def start_game():
    """
    업다운 게임 시작 함수
    - 게임 여부를 묻고, 난이도를 선택한 뒤 게임을 진행
    - 1~100 사이의 숫자를 맞추는 게임
    """

    # 게임 시작 여부를 묻는다
    play_game = input("게임을 시작하시겠습니까? (y/n): ").lower()
    if play_game != 'y':
        print("게임을 종료합니다.")
        return

    print(logo)  # 게임 로고 출력

    # 난이도를 선택한다
    difficulty = input("난이도를 선택하세요: Easy(10번) 또는 Hard(5번): ").lower()
    attempts = 10 if difficulty == 'easy' else 5  # Easy: 10회, Hard: 5회
    print(f"{attempts}번의 기회가 주어집니다!")

    # 임의의 숫자를 생성
    target = random.randint(1, 100)

    # 게임 진행
    for attempt in range(1, attempts + 1):
        try:
            # 사용자 입력
            guess = int(input(f"숫자를 입력하세요 (1~100): "))

            # 유효성 검사: 1~100 범위 확인
            if guess < 1 or guess > 100:
                print("1에서 100 사이의 숫자를 입력해주세요.")
                continue

            # 업다운 힌트 제공
            if guess < target:
                print("UP!")  # 입력값이 정답보다 작음
            elif guess > target:
                print("DOWN!")  # 입력값이 정답보다 큼
            else:
                print(f"축하합니다! 정답입니다. {attempt}번 만에 맞추셨습니다!")  # 정답
                break
        except ValueError:
            print("유효한 숫자를 입력해주세요.")  # 숫자가 아닌 값 처리
            continue

        # 모든 시도 후 실패 시 메시지 출력
        if attempt == attempts:
            print(f"기회를 모두 사용하셨습니다. 실패! 정답은 {target}이었습니다.")

# 게임 실행
start_game()
import random
from art import logo, vs
from game_data import data

# 두 명의 인물을 랜덤으로 선택하는 함수
def get_random_account():
    return random.choice(data)

# 인물 정보를 포맷팅해서 문장 출력
def format_account(account):
    """인물정보를 포멧팅해보자"""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

# 두 인물의 팔로워 수를 비교하는 함수
def check_answer(guess_user, a_followers, b_followers):
    """사용자의 추측이 정답인지 확인"""
    if a_followers > b_followers:
        return guess_user == "a"
    else:
        return guess_user == "b"


def game():
    print(logo)
    score = 0
    game_should_continue = True
    # b만 만들어서 a로 보내준다.
    account_b = get_random_account()


    while game_should_continue:
        # account_b를 account_a로 업데이트하고 새로운 account_b 선택
        account_a = account_b
        account_b = get_random_account()

        # 같은 계정이 선택되지 않도록 방지
        while account_a == account_b:
            account_b = get_random_account()

        # 선택된 두 명(A, B)을 비교하는 문장을 출력합니다.
        print(f"Compare A: {format_account(account_a)}")
        print(vs)
        print(f"Against B: {format_account(account_b)}")

        # 사용자의 입력(A 또는 B)을 확인하고, 두 사람의 팔로워 수를 비교합니다.
        guess = input("Who has more followers? Type 'A' or 'B':").lower()
        
        # 화면 지우기
        print("\n" * 20)
        print(logo)

        # 올바르면 점수를 올리고 다음 라운드로 이동합니다.
        # 틀리면 게임 종료.
        # 다음 라운드로 진행한다.
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]

        # 정답 확인
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        # 이전 라운드에서 B가 A로 바뀌고, 새로운 B를 선택합니다.
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}.")


# 게임 실행
game()
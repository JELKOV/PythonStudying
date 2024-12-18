import random
from art import logo

# 카드 덱: Ace는 11로, Jack, Queen, King은 10으로 처리
card_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    """
    카드 덱에서 무작위로 카드 한 장을 뽑아 반환합니다.
    """
    return random.choice(card_deck)

def calculate_score(deck):
    """
    카드 덱의 점수를 계산합니다.
    - 블랙잭(2장의 카드로 21점)이면 0 반환
    - Ace(11)가 포함되어 있고 총 점수가 21점을 초과하면 Ace를 1로 바꿉니다.
    """
    score = sum(deck)  # 현재 카드 점수 합계 계산

    # 블랙잭 확인: 2장의 카드로 21점
    if score == 21 and len(deck) == 2:
        return 0  # 블랙잭의 점수는 0으로 처리

    # Ace 처리: 점수가 21 초과 시 Ace를 11에서 1로 변경
    if 11 in deck and score > 21:
        deck.remove(11)  # Ace(11)를 덱에서 제거
        deck.append(1)   # Ace를 1로 추가

    return sum(deck)  # 최종 점수 반환

def compare(u_score, d_score):
    """
    사용자 점수와 딜러 점수를 비교하여 결과 메시지를 반환합니다.
    """
    if u_score == d_score:
        return "무승부입니다."  # 점수가 같을 경우
    elif d_score == 0:
        return "딜러가 블랙잭입니다. 패배!"  # 딜러가 블랙잭
    elif u_score == 0:
        return "블랙잭입니다! 승리!"  # 사용자가 블랙잭
    elif u_score > 21:
        return "21을 초과했습니다. 패배!"  # 사용자가 21 초과
    elif d_score > 21:
        return "딜러가 21을 초과했습니다. 승리!"  # 딜러가 21 초과
    elif u_score > d_score:
        return "승리했습니다!"  # 사용자가 딜러보다 높은 점수
    else:
        return "패배했습니다."  # 그 외의 경우 딜러 승리

# 게임 시작 루프
while input("게임을 시작하시겠습니까? 'y' 또는 'n': ") == 'y':
    print(logo)  # 로고 출력

    # 초기 카드 2장씩 분배
    user_deck = [deal_card(), deal_card()]  # 사용자 카드
    dealer_deck = [deal_card(), deal_card()]  # 딜러 카드

    # 초기 점수 계산
    user_score = calculate_score(user_deck)
    dealer_score = calculate_score(dealer_deck)

    # 게임 종료 플래그
    game_over = False

    # 사용자 턴
    while not game_over:
        print(f"사용자 카드: {user_deck}, 점수: {user_score}")
        print(f"딜러의 첫 번째 카드: {dealer_deck[0]}")  # 딜러의 첫 카드만 공개

        # 블랙잭 또는 점수 초과 시 사용자 턴 종료
        if user_score == 0 or dealer_score == 0 or user_score > 21:
            game_over = True
        else:
            # 추가 카드를 받을지 선택
            user_choice = input("카드를 더 받으시겠습니까? 'y' 아니면 'n': ")
            if user_choice == 'y':
                user_deck.append(deal_card())  # 카드 한 장 추가
                user_score = calculate_score(user_deck)  # 점수 재계산
            else:
                game_over = True  # 사용자 턴 종료

    # 딜러 턴: 점수가 17 미만일 경우 계속 카드 추가
    while dealer_score != 0 and dealer_score < 17:
        dealer_deck.append(deal_card())  # 카드 추가
        dealer_score = calculate_score(dealer_deck)  # 점수 재계산

    # 최종 결과 출력
    print(f"\n사용자 카드: {user_deck}, 최종 점수: {user_score}")
    print(f"딜러 카드: {dealer_deck}, 최종 점수: {dealer_score}")
    print(compare(user_score, dealer_score))  # 사용자와 딜러 점수 비교 결과 출력

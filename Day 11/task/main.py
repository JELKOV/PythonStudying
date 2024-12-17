import random

# 카드 덱: 11은 Ace를 의미하고, 10은 Jack, Queen, King을 포함합니다.
card_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    """카드 덱에서 무작위로 카드 한 장 뽑기"""
    return random.choice(card_deck)  # 랜덤으로 카드 한 장을 반환

def calculate_score(deck):
    """
    입력된 카드 덱의 점수를 계산합니다.
    - 블랙잭(2장의 카드로 21점)이면 0을 반환합니다.
    - Ace(11)가 포함되어 있고 총점이 21점을 초과하면 Ace를 1로 바꿉니다.
    """
    score = sum(deck)  # 카드 점수의 합계 계산

    # 블랙잭 확인 (2장의 카드가 21점일 경우)
    if score == 21 and len(deck) == 2:
        return 0  # 블랙잭은 점수를 0으로 처리

    # Ace가 포함되어 있고 점수가 21을 초과하면 Ace를 1로 변경
    if 11 in deck and score > 21:
        deck.remove(11)  # Ace(11)를 제거
        deck.append(1)   # Ace를 1로 추가

    return sum(deck)  # 최종 점수 반환

def compare(u_score, d_score):
    """
    사용자와 딜러의 점수를 비교해 결과를 반환합니다.
    """
    if u_score == d_score:
        return "무승부입니다."  # 점수가 같으면 무승부
    elif d_score == 0:
        return "딜러가 블랙잭입니다. 패배!"  # 딜러가 블랙잭일 경우
    elif u_score == 0:
        return "블랙잭입니다! 승리!"  # 사용자가 블랙잭일 경우
    elif u_score > 21:
        return "21을 초과했습니다. 패배!"  # 사용자의 점수가 21 초과
    elif d_score > 21:
        return "딜러가 21을 초과했습니다. 승리!"  # 딜러의 점수가 21 초과
    elif u_score > d_score:
        return "승리했습니다!"  # 사용자의 점수가 더 높을 경우
    else:
        return "패배했습니다."  # 그 외의 경우 패배

# 게임 시작
while input("게임을 시작하시겠습니까? 'y' 또는 'n': ") == 'y':
    # 초기 카드 두 장씩 뽑기
    user_deck = [deal_card(), deal_card()]  # 사용자 카드 덱
    dealer_deck = [deal_card(), deal_card()]  # 딜러 카드 덱

    # 초기 점수 계산
    user_score = calculate_score(user_deck)
    dealer_score = calculate_score(dealer_deck)

    # 게임 종료 플래그
    game_over = False

    # 사용자 턴
    while not game_over:
        print(f"사용자 카드: {user_deck}, 점수: {user_score}")
        print(f"딜러의 첫 번째 카드: {dealer_deck[0]}")  # 딜러는 첫 번째 카드만 공개

        # 게임 종료 조건: 블랙잭이거나 점수가 21 초과일 경우
        if user_score == 0 or dealer_score == 0 or user_score > 21:
            game_over = True
        else:
            # 사용자에게 카드 추가 여부를 물어봄
            user_choice = input("카드를 더 받으시겠습니까? 'y' 아니면 'n': ")
            if user_choice == 'y':
                user_deck.append(deal_card())  # 카드 한 장 추가
                user_score = calculate_score(user_deck)  # 새로운 점수 계산
            else:
                game_over = True  # 더 이상 카드를 받지 않으면 게임 종료

    # 딜러 턴: 딜러의 점수가 17 미만일 경우 계속해서 카드 뽑기
    while dealer_score != 0 and dealer_score < 17:
        dealer_deck.append(deal_card())  # 딜러가 카드 한 장 추가
        dealer_score = calculate_score(dealer_deck)  # 딜러 점수 다시 계산

    # 최종 결과 출력
    print(f"\n사용자 카드: {user_deck}, 최종 점수: {user_score}")
    print(f"딜러 카드: {dealer_deck}, 최종 점수: {dealer_score}")
    print(compare(user_score, dealer_score))  # 점수 비교 및 결과 출력

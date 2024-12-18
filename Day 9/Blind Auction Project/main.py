# Blind Auction 프로그램 시작
from art import logo
print(logo)

# 빈 딕셔너리로 입찰 정보 저장
bid_dic = {}

# 딕셔너리에서 최고 입찰자 찾는 함수 정의
def add_dic(dictionary):
    highest_bid = 0
    winner = ""
    # 딕셔너리 순회하며 최고 입찰자 찾기
    for bidder in dictionary:
        bid_amount = dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

# 입찰 진행 여부를 나타내는 플래그
bidding_finished = False

# 입찰 루프
while not bidding_finished:
    # 사용자 입력 받아서 이름과 가격 저장
    name = input("이름을 적어주세요: ")
    price = int(input("가격을 입력하세요: $"))

    bid_dic[name] = price  # 딕셔너리에 추가

    # 다른 참여자 여부 확인
    should_continue = input("다른 참여자가 있나요?? ex) 'yes' or 'no': ").lower()
    if should_continue == "no":
        bidding_finished = True  # 입찰 종료
        add_dic(bid_dic)  # 최고 입찰자 출력
    elif should_continue == "yes":
        print("\n" * 100)  # 화면 초기화

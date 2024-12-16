from art import logo
print(logo)
bid_dic = {}

def add_dic(dictionary):
    highest_bid = 0
    winner = ""
    for bidder in dictionary:
        bid_amount = dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

bidding_finished = False
while not bidding_finished:
    name = input("이름을 적어주세요")
    price = int(input("가격을 입력하세요: $"))

    bid_dic[name] = price

    should_continue = input("다른 참여자가 있나요?? ex) 'yes' or 'no': ").lower()
    if should_continue == "no":
        bidding_finished = True
        add_dic(bid_dic)
    elif should_continue == "yes":
        print("\n" * 100)




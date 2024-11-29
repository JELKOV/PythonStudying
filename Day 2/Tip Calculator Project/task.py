# Welcome 메시지 출력
print("Welcome to the tip calculator!")

# 사용자로부터 입력값 받기
bill = float(input("What was the total bill? $"))  # 총 금액
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))  # 팁 퍼센트
people = int(input("How many people to split the bill? "))  # 나눌 사람 수

# 팁 계산
tip_multiplier = 1 + (tip / 100)
total_bill = bill * tip_multiplier

# 각 사람당 지불할 금액 계산
amount_per_person = total_bill / people

# 소수점 둘째 짜리
final_amount = round(amount_per_person, 2)
print(f"Each Person should pay: ${final_amount}")

# 소수점 둘째 자리까지 반올림하여 출력
formatted_amount = "{:.2f}".format(amount_per_person)
print(f"Each person should pay: ${formatted_amount}")

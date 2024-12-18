import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


# 게임 이미지 리스트 (rock, paper, scissors는 정의된 변수로 가정)
game_images = [rock, paper, scissors]

# 사용자 입력 받기
user_choice = int(input("What do you choose? Type 0 Rock, Type 1 Papper, Type 2 Scissors "))

# 유효한 입력인지 확인 (0~2 범위)
if user_choice >= 0 and user_choice <= 2:
    print(game_images[user_choice])  # 사용자 선택 출력

# 컴퓨터 랜덤 선택
computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])  # 컴퓨터 선택 출력

# 잘못된 입력 처리
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
# 승리 조건 확인
elif user_choice == 0 and computer_choice == 2:
    print("승리")  # 사용자가 바위, 컴퓨터가 가위
elif computer_choice == 0 and user_choice == 2:
    print("패배!")  # 사용자가 가위, 컴퓨터가 바위
elif computer_choice > user_choice:
    print("You lose!")  # 컴퓨터가 사용자를 이김
elif user_choice > computer_choice:
    print("You win!")  # 사용자가 컴퓨터를 이김
else:
    print("It's a draw!")  # 무승부
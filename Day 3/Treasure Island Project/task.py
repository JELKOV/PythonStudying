print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
# Treasure Island 어드벤처 게임
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# 첫 번째 선택지
choice1 = input('너는 왼쪽으로 갈거니 오른쪽으로 갈거니? Type "left" or "right": ').lower()

# "left"를 선택한 경우
if choice1 == "left":
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. '
                    'Type "wait" to wait for a boat. Type "swim" to swim across: ').lower()

    # "wait"를 선택한 경우
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. "
                        "One red, one yellow and one blue. Which colour do you choose? ").lower()

        # 선택한 문에 따라 결과 출력
        if choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure. You Win!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You got attacked by an angry trout. Game Over.")  # "swim" 선택 시 실패
else:
    print("You fell into a hole. Game Over.")  # "right" 선택 시 실패

import random  # 랜덤 단어 선택을 위한 모듈
import hangman_words  # 단어 리스트를 포함한 사용자 정의 모듈
import hangman_art  # 행맨 게임 시각적 요소를 포함한 사용자 정의 모듈

# TODO-1: - 'hangman_words.py'에서 'word_list' 가져오기
from hangman_words import word_list  # 단어 리스트 가져오기
from hangman_art import stages, logo  # 행맨 로고와 단계 이미지 가져오기

# 사용자에게 제공할 목숨 수 초기화
lives = 6

# TODO-3: - 'hangman_art.py'에서 가져온 로고를 게임 시작 시 출력
print(logo)  # 행맨 게임 로고 출력

# 랜덤 단어 선택
chosen_word = random.choice(word_list)
print(chosen_word)  # 선택된 단어 출력 (디버깅용)

# 단어 길이에 맞는 밑줄 생성
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)  # 밑줄로 표현된 단어 출력

# 게임 상태 초기화
game_over = False
correct_letters = []  # 맞춘 문자 저장
incorrect_letters = []  # 틀린 문자 저장

# 게임 루프
while not game_over:

    # TODO-6: - 남은 목숨 수를 사용자에게 출력
    print(f"You have {lives} lives remaining.")

    # 사용자로부터 문자 입력받기
    guess = input("Guess a letter: ").lower().strip()

    # 현재까지 맞춘 문자와 틀린 문자 출력
    print(f"Correct letters so far: {correct_letters}")
    print(f"Incorrect letters so far: {incorrect_letters}")

    # TODO-4: - 이미 입력한 문자를 다시 입력했는지 확인
    if not guess:
        print("You must enter a valid letter. Try again.")
        continue

    if guess in correct_letters or guess in incorrect_letters:
        print(f"Already guessed {guess}. Try different words.")
        continue

    # 사용자 입력에 따라 단어 상태 업데이트
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)  # 현재 단어 상태 출력

    # TODO-5: - 틀린 문자를 입력했을 때 사용자에게 알리고 목숨을 줄이기
    if guess in chosen_word:
        correct_letters.append(guess)  # 맞춘 문자에 추가
    else:
        lives -= 1  # 목숨 감소
        incorrect_letters.append(guess)  # 틀린 문자에 추가
        print(f"You guessed '{guess}', which is not in the word. You lose a life.")

        # 목숨이 0이 되면 게임 종료
        if lives == 0:
            game_over = True

            # TODO 7: - 실패 시 정답 단어를 사용자에게 출력
            print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")

    # 단어가 완전히 맞춰졌을 경우 게임 종료
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    # TODO-2: - 행맨 단계를 'hangman_art.py'의 stages 리스트를 사용하여 출력
    print(stages[lives])  # 현재 목숨 상태에 맞는 이미지 출력

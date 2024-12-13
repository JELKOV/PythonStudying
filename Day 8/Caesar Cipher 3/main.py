# TODO-1: Import and print the logo from art.py when the program starts.
from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-2: What happens if the user enters a number/symbol/space?


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    for letter in original_text:
        if letter in alphabet:
            if encode_or_decode == "decode":
                shift_amount *= -1

            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
        else:
            output_text+=letter
    print(f"Here is the {encode_or_decode}d result: {output_text}")


# TODO-3: Can you figure out a way to restart the cipher program?

# 프로그램 시작 및 반복 실행
def start_cipher():
    while True:  # 무한 반복으로 프로그램 재시작 가능
        # 사용자 입력
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n")) % len(alphabet)  # 큰 shift 값 처리

        # Caesar 함수 호출
        caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

        # 재시작 여부 확인
        restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
        if restart != "yes":
            print("Goodbye!")
            break  # 반복 종료 및 프로그램 종료


# 프로그램 실행
start_cipher()




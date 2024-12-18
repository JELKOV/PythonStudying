# TODO-1: art.py 모듈에서 logo를 가져오고 출력합니다.
# Caesar Cipher 프로그램의 로고를 표시합니다.
from art import logo
print(logo)

# 알파벳 리스트 정의 (a-z)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Caesar 암호화 및 복호화 함수
def caesar(original_text, shift_amount, encode_or_decode):
    """
    Caesar 암호화/복호화 함수
    :param original_text: 암호화/복호화할 텍스트
    :param shift_amount: 이동할 문자 수
    :param encode_or_decode: 'encode' 또는 'decode' 여부
    """
    output_text = ""  # 결과 메시지를 저장할 문자열

    # 입력 텍스트의 각 문자 처리
    for letter in original_text:
        if letter in alphabet:  # 알파벳에 포함된 문자만 처리
            # 복호화 시, 이동 값을 반대로 설정
            if encode_or_decode == "decode":
                shift_amount *= -1

            # 문자 위치를 이동
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)  # 알파벳 길이를 넘어가면 순환 처리
            output_text += alphabet[shifted_position]  # 결과 문자열에 추가
        else:
            # 알파벳이 아닌 문자는 그대로 추가
            output_text += letter

    # 결과 출력
    print(f"Here is the {encode_or_decode}d result: {output_text}")


# TODO-3: 프로그램을 재시작할 수 있도록 반복 실행 기능 추가
def start_cipher():
    """
    Caesar Cipher 프로그램을 시작하고 재시작할 수 있도록 반복 실행
    """
    while True:  # 무한 반복으로 프로그램 재시작 가능
        # 사용자로부터 입력값 받기
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()  # 암호화 또는 복호화 선택
        text = input("Type your message:\n").lower()  # 암호화/복호화할 메시지 입력
        shift = int(input("Type the shift number:\n")) % len(alphabet)  # 큰 shift 값을 알파벳 길이로 순환 처리

        # Caesar 함수 호출
        caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

        # 프로그램 재시작 여부 확인
        restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
        if restart != "yes":  # "yes"가 아닌 입력 시 프로그램 종료
            print("Goodbye!")
            break  # 반복 종료 및 프로그램 종료


# 프로그램 실행
start_cipher()

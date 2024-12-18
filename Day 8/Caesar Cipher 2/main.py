# 알파벳 리스트 정의 (a-z)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# 사용자가 암호화 또는 복호화 선택
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

# 사용자가 암호화할 메시지 입력
text = input("Type your message:\n").lower()

# 이동할 문자 수 입력
shift = int(input("Type the shift number:\n"))

# # 이전 암호화 함수 (암호화만 가능)
# def encrypt(original_text, shift_amount):
#     cipher_text = ""  # 암호화된 메시지를 저장할 문자열
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) + shift_amount  # 현재 문자 위치를 이동
#         shifted_position %= len(alphabet)  # 알파벳 길이를 넘어가면 순환 처리
#         cipher_text += alphabet[shifted_position]  # 결과 문자열에 추가
#     print(f"Here is the encoded result: {cipher_text}")  # 암호화 결과 출력
#
# encrypt(original_text=text, shift_amount=shift)  # 함수 호출

# # TODO-1: 복호화 함수 'decrypt()' 생성
# def decrypt(original_text, shift_amount):
#     decoded_text = ""  # 복호화된 메시지를 저장할 문자열
#     for letter in original_text:
#         back_position = alphabet.index(letter) - shift_amount  # 현재 문자 위치를 반대로 이동
#         back_position %= len(alphabet)  # 알파벳 길이를 넘어가면 순환 처리
#         decoded_text += alphabet[back_position]  # 결과 문자열에 추가
#     print(f"Here is the decoded result: {decoded_text}")  # 복호화 결과 출력

# TODO-3: 암호화와 복호화 통합 함수 'caesar()' 생성
def caesar(original_text, shift_amount, encode_or_decode):
    """
    Caesar 암호화/복호화 함수
    :param original_text: 암호화/복호화할 텍스트
    :param shift_amount: 이동할 문자 수
    :param encode_or_decode: 'encode' 또는 'decode' 여부
    """
    output_text = ""  # 결과 메시지를 저장할 문자열
    for letter in original_text:
        # 복호화 시, 이동 값을 반대로 변경
        if encode_or_decode == "decode":
            shift_amount *= -1

        # 문자 위치를 이동
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)  # 알파벳 길이를 넘어가면 순환 처리
        output_text += alphabet[shifted_position]  # 결과 문자열에 추가

    # 결과 출력
    print(f"Here is the {encode_or_decode}d result: {output_text}")

# 사용자 입력에 따라 암호화 또는 복호화 실행
caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

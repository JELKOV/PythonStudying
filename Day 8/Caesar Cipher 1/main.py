alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# 사용자가 암호화 또는 복호화를 선택
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()  # 메시지 입력
shift = int(input("Type the shift number:\n"))  # 이동할 문자 수 입력

# 암호화 함수
def encrypt(original_text, shift_amount):
    encrypted_text = ""
    for letter in original_text:
        if letter in alphabet:  # 알파벳인 경우에만 처리
            current_index = alphabet.index(letter)  # 현재 위치 확인
            new_index = (current_index + shift_amount) % len(alphabet)  # 이동 후 위치
            encrypted_text += alphabet[new_index]  # 암호화된 문자 추가
        else:
            encrypted_text += letter  # 알파벳이 아닌 경우 그대로 추가
    print(f"Here is the encoded result: {encrypted_text}")

# 암호화 요청 시 실행
if direction == "encode":
    encrypt(original_text=text, shift_amount=shift)
else:
    print("Invalid direction. Only 'encode' is supported in this demo.")

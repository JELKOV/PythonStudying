alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.


def encrypt(original_text, shift_amount):
    encrypted_text=""
    for letter in original_text:
        if letter in alphabet:  # 알파벳에 있는 문자만 암호화
            current_index = alphabet.index(letter)
            new_index = (current_index + shift_amount) % len(alphabet)  # 순환 처리
            encrypted_text += alphabet[new_index]
        else:
            encrypted_text += letter  # 알파벳이 아닌 문자는 그대로 추가
        print(f"Here is the encoded result: {encrypted_text}")
# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.
if direction == "encode":
    encrypt(original_text=text, shift_amount=shift)
else:
    print("Invalid direction. Only 'encode' is supported in this demo.")
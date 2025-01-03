# 숫자와 문자열 변환 예시
print("My age: " + str(12))  # 정수를 문자열로 변환하여 출력
print(123 + 456)  # 덧셈 연산 (579)
print(7 - 3)      # 뺄셈 연산 (4)
print(3 * 2)      # 곱셈 연산 (6)
print(5 / 3)      # 나눗셈 (결과는 실수형 1.666...)
print(5 // 3)     # 몫만 반환하는 나눗셈 (1)
print(2 ** 3)     # 거듭제곱 연산 (2의 3승 = 8)

# PEMDAS (연산 우선순위)
# 괄호 -> 지수 -> 곱셈/나눗셈 -> 덧셈/뺄셈 순서
print(3 * 3 + 3 / 3 - 3)  # 결과: 7
print(3 * 3 + 3 / 3 - 3)  # 같은 식, 결과: 7
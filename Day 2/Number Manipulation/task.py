# BMI (체질량지수) 계산 예시
bmi = 84 / 1.65 ** 2  # 체중(kg) / 키(m)의 제곱
print(bmi)            # BMI 실수 값 출력
print(int(bmi))       # 정수로 변환하여 출력
print(round(bmi))     # 반올림된 값 출력
print(round(bmi, 2))  # 소수점 둘째 자리까지 반올림하여 출력

# Assignment Operators (대입 연산자)
score = 0
score += 2  # score에 2를 더함
print(score)  # 출력: 2

score /= 2  # score를 2로 나눔
print(score)  # 출력: 1.0

# f-Strings (포맷 문자열)
print(f"Your score is = {score}")  # 변수 값을 문자열에 삽입하여 출력
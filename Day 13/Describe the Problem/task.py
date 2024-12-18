def my_function():
    num = 0  # 숫자를 증가시키기 위한 초기값 설정
    for i in range(1, 20):  # 1부터 19까지 반복
        num += 1  # num 값을 1씩 증가
        print(f"check{num}")  # 현재 num 값을 출력
        if i == 20:  # i가 20일 경우에만 실행 (하지만 20은 반복 범위에 포함되지 않음)
            print("You got it")  # 메시지 출력

my_function()

# Describe the Problem - Write your answers as comments:

# 1. What is the for loop doing?
#    - for 루프는 1부터 19까지의 숫자를 순서대로 반복하며, num 값을 증가시키고 해당 값을 출력합니다.

# 2. When is the function meant to print "You got it"?
#    - 함수는 i가 20일 때 "You got it"을 출력하도록 작성되어 있지만, 반복 범위(1~19)에는 20이 포함되지 않으므로 해당 메시지가 출력되지 않습니다.

# 3. What are your assumptions about the value of i?
#    - i는 1부터 시작하여 19까지 반복되며, 20은 포함되지 않습니다. 따라서 i == 20 조건은 실행되지 않습니다.

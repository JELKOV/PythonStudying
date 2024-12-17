from art import logo


def add(n1, n2):
    return n1 + n2

# my_favorite_operation = add
#
# print(my_favorite_operation(3,5))


# Todo: 3 function - subtract, multiple, divide

def subtract(n1, n2):
    return n1 - n2

def multiple(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# Todo: 4 function into dictionary

operator_dic = {
    "+": add,
    "-": subtract,
    "*": multiple,
    "/": divide
}

# Todo: Using operation_dic to calculation
# num1 = 4
# num2 = 8
# print(operator_dic["*"](num1, num2))


def calculator():
    print(logo)
    stop_signal = False
    result = 0

    # 첫 번째 숫자 입력 (반복 시작 전에 초기화)
    first_num = float(input("첫 번째 숫자를 입력하세요: "))


    while not stop_signal:
    # 연산자 입력
    # 프로그램이 사용자에게 수학 연산자를 입력하도록 요청합니다.
    # (연산자는 "+", "-", "*", "/" 중 하나를 선택합니다.)
        choose_operation = input("연산자를 입력하세요 : +, -, *, /")

    # 두 번째 숫자 입력
    # 프로그램이 사용자에게 두 번째 숫자를 입력하도록 요청합니다.
        second_num = float(input("두번째 숫자를 입력하세요"))

    # 계산 실행
    # 사용자가 선택한 연산자에 따라 첫 번째 숫자와 두 번째 숫자를 계산하고 결과를 출력합니다.
        result = operator_dic[choose_operation](first_num, second_num)
        print(f"현재 결과값{result}")
    # 이전 결과 계속 사용 여부 확인
    # 프로그램이 사용자에게 이전 결과를 계속 사용할지 묻습니다.
        continue_or_not = input("계속 계산하시겠습니까?: 예/아니오").strip()

    # "네"라고 응답하면, 이전 결과를 첫 번째 숫자로 사용하여 다시 계산을 진행합니다.
    # "아니오"라고 응답하면, 이전 결과를 지우고 처음부터 다시 시작합니다.
    # 반복 실행
    # 사용자가 계산을 계속하고 싶을 때까지 프로그램은 이 과정을 반복합니다.
        if continue_or_not == "아니오":
            stop_signal = True
            print("계산기를 종료합니다.")
            calculator() #재귀함수
        elif continue_or_not =="예":
            first_num = result
        else:
            print("잘못된 입력입니다 : 예/ 아니오")
    # 로고 추가
    # 프로그램의 시작 부분에 art.py 파일에 있는 로고를 표시합니다.
calculator()
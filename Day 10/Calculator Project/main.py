# art.py의 로고를 출력
from art import logo

def add(n1, n2):
    # 두 숫자를 더하는 함수
    return n1 + n2

def subtract(n1, n2):
    # 두 숫자를 빼는 함수
    return n1 - n2

def multiple(n1, n2):
    # 두 숫자를 곱하는 함수
    return n1 * n2

def divide(n1, n2):
    # 두 숫자를 나누는 함수
    return n1 / n2

# 연산자와 함수를 매핑하는 딕셔너리
operator_dic = {
    "+": add,
    "-": subtract,
    "*": multiple,
    "/": divide
}

def calculator():
    # 로고 출력
    print(logo)
    stop_signal = False

    # 첫 번째 숫자 입력
    first_num = float(input("첫 번째 숫자를 입력하세요: "))

    while not stop_signal:
        # 연산자 입력
        choose_operation = input("연산자를 입력하세요 : +, -, *, /")

        # 두 번째 숫자 입력
        second_num = float(input("두번째 숫자를 입력하세요"))

        # 연산 결과 계산
        result = operator_dic[choose_operation](first_num, second_num)
        print(f"현재 결과값: {result}")

        # 계산 계속 여부 확인
        continue_or_not = input("계속 계산하시겠습니까?: 예/아니오").strip()

        if continue_or_not == "아니오":
            # 계산 종료 및 초기화
            stop_signal = True
            print("계산기를 종료합니다.")
            calculator()  # 재귀 호출로 새 계산기 실행
        elif continue_or_not == "예":
            # 이전 결과값을 다음 계산에 사용
            first_num = result
        else:
            # 잘못된 입력 처리
            print("잘못된 입력입니다 : 예/아니오")

# 계산기 실행
calculator()
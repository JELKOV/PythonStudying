def format_name(f_name, l_name):
    # 이름과 성이 빈 문자열일 경우 에러 메시지 반환
    if f_name == "" and l_name == "":
        return "입력값이 없습니다"
    # 이름과 성을 포맷팅하여 반환
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"

# 사용자 입력을 받아 포맷팅된 이름 출력
print(format_name(input("성이 뭐에요"), input("이름이 뭐에요")))

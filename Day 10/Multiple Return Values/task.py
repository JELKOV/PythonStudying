def format_name(f_name, l_name):
    if f_name == "" and l_name == "":
        return "입력값이 없습니다"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"


print(format_name(input("성이 뭐에요"), input("이름이 뭐에요")))

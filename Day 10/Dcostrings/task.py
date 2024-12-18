def format_name(f_name, l_name):
    """이름과 성을 입력받아 첫 글자를 대문자로 포맷팅하여 반환"""
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

# 이름을 포맷팅하고 길이를 확인
formatted_name = format_name("AnGeLa", "YU")
length = len(formatted_name)
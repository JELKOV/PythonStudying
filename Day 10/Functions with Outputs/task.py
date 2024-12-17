def format_name(f_name, l_name):
    return f"{f_name.title()} {l_name.title()}"

formatting_string = format_name("ahn", "jaeho")

print(formatting_string)


# output = len("AHN")

def function_1(text):
    return text + text

def functino_2(text):
    return text.title()



output = function_1("HELLO")
output1 = functino_2(function_1("HELLO"))

print(output)
print(output1)
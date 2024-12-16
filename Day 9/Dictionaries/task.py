programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

print(programming_dictionary["Bug"])
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

empty_dictionary = {}


# 초기화
# programming_dictionary = empty_dictionary
#
# print(programming_dictionary)

# 수정
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)


# 반복 정의
for thing in programming_dictionary:
    print(thing)
    print(programming_dictionary[thing])
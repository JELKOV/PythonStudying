len("Hello")

# Type Error
# len(12345) XXXXX
# 괄호 안에 넣는 인수는 문자열, 바이트 ,듀플 ,딕셔너리 세트 컬렉션만 된다


#Type Checking
print(type("Hello"))
print(type(123))
print(type(True))
print(type(1.2313))

#Type Conversion
print(int("123") + int("456"))

name_of_the_user = input("Enter your name")

length_of_the_name= len(name_of_the_user)

print("Number of letters in your name: " + str(length_of_the_name) )
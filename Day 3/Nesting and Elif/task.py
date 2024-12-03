print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?"))
    if age <= 12:
        print("5불 내세요")
    elif age <= 18:
        print("7불 내세요")
    else:
        print("12불 내세요")
else:
    print("Sorry you have to grow taller before you can ride.")

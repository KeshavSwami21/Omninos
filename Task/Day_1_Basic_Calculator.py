def logic(str):
    lst = str.split(" ")
    # print(lst)
    divi1 = []
    divi2 = []
    try:
        for i in lst[0]:
            divi1.append(i)
        for i in lst[2]:
            divi2.append(i)
    except:
        print("error")

    if lst[1] == "+":
        print(f"Addition of two numbers is: {int(lst[0]) + int(lst[2])}")
    elif lst[1] == "-":
        print(f"Substraction of two numbers is: {int(lst[0]) - int(lst[2])}")
    elif lst[1] == "*" or lst[1] == "x":
        print(f"Multiplication of two numbers is: {int(lst[0]) * int(lst[2])}")
    elif lst[1] == "/":
        if lst[0] == '0':
            print(f"The division of two numbers is {0} because the numenator is {0}.")
        elif lst[2] == '0':
            print(f"The division is undefined/infinity because the denominator is {0}.")
        elif ("." in divi1) or ("." in divi2):
            print("Division of two numbers is: ", float(lst[0]) / float(lst[2]))
        else:
            print("Division of two numbers is: ", int(lst[0]) // int(lst[2]))


str = input(
    "Enter the Basic two calculation string with each character saprated by whitespace.\nOnly Addition, Subtraction, Multiplication and Division are supported at this time.\nSo Enter your numbers: "
)

logic(str)


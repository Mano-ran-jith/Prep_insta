# Greatest of three numbers

def three_great():
    num1 = 10
    num2 = 20
    num3 = 30
    if num1>num2 and num1>num3:
        print(num1)
    elif num2>num3:
        print(num2)
    else:
        print(num3)
three_great()

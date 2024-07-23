#gretest of two numbers

def gretest_num():

    num1 = 10
    num2 = 30
    if num1 > num2:
        print(num1)
    else:
        print(num2)

    print(num1 if num1 > num2 else num2)
gretest_num()

# Sum of digits of a number

def sum_digits():
    Digi = input("enter a num: ")
    res = 0
    for i in Digi:
        res = res + int(i)
    print(res)
sum_digits()
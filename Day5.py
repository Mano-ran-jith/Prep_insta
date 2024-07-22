# Range sum of btw num

def sumofrange():
    num1 = int(input())
    num2 = int(input())
    sum = 0
    for i in range(num1,num2):
        sum += i
    print(sum)
sumofrange()

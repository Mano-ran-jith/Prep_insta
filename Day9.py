#prime number

def prime_num():
    num = 4
    res = 0
    for i in range(2,num):
        if num%i == 0:
            res = 1
            break
    if res == 1:
            print("Not Prime")
    else:
            print("Prime")
prime_num()

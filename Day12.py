# Reverse of a number

def reverse_num():
    user = int(input("Enter a num: "))
    temp = user
    reverse = 0
    while user > 0:
        reminder = user % 10
        reverse = (reverse * 10) + reminder
        user = user // 10
    print(reverse)
reverse_num()
        
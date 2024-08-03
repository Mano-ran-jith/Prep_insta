#Palindrome number

num = 122
temp = num
reverse = 0
while temp > 0:
    reminder = temp % 10 #here we have last number of "NUM"
    reverse = (reverse*10)+reminder #round the value and add reminder ((0*10)+1 = 1)
    temp = temp // 10 #remove the last value of "NUM"
    
if num == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")
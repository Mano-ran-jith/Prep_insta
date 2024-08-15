#Amstrong Number or Not

num1 = 371
num3 = 0
for i in str(num1):
    num2 = len(str(num1))
    num3 += (int(i) ** num2)
if num1 == num3:
    print("Amstrong Number")
else:
    print("Not an Amstrong")

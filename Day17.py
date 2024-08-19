# Input: Nth term to find
N = int(input("Enter the position of the Fibonacci term: "))

a = 0
b = 1

if N == 1:
    print(a)
elif N == 2:
    print(b)
else:
    for i in range(3, N + 1):
        c = a + b
        a = b
        b = c

    print(b)


#0 (1st term)
#1 (2nd term)
#1 (3rd term) → 0 + 1
#2 (4th term) → 1 + 1
#3 (5th term) → 1 + 2
#5 (6th term) → 2 + 3
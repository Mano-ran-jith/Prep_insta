# Amstrong number in given range

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

armstrong_numbers = []

for num in range(start, end + 1):
    num_str = str(num)
    power = len(num_str)
    total = 0
    
    for digit in num_str:
        total += int(digit) ** power
    
    if num == total:
        armstrong_numbers.append(num)

print(f"Armstrong numbers between {start} and {end}: {armstrong_numbers}")

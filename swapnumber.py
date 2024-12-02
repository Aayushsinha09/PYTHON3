n = 20
num1 = 20
num2 = 30
next_number = num1 
count = 1

while count <= n:
    print(next_number, end=" ")
    count += 2
    num1, num2 = num2, next_number
    next_number = num1 + num2
print()
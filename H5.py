# Question2

num = int(input("Number in Binary ="))
c = 0
result = 0
while num != 0:
    result = result + (num % 10)*(2**c)
    num = num//10
    c += 1
print("Number in decimal =", result)

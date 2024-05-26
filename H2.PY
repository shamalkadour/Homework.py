# B
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


N = int(input("Enter the number for calculate factorial:"))

if N < 0:
    print("Factoriality doesnt count for negative numbers")
else:
    f = factorial(N)
    print(f" the factoriality {N} is {f}")

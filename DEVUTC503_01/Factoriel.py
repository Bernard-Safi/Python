def factorial(n):
    fact = 1;
    for num in range(2, n + 1):
        fact *= num;
    return fact;

def factorialrec(n):
    if n < 2:
        return 1
    else:
        return n * factorialrec(n-1)

print(factorial(5));
print(factorialrec(6));

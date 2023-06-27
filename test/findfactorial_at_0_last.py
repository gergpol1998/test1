def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while(n > 1):
            fact *= n
            n -= 1
        return fact

def factendzero(n):
    x = n // 5
    y = x
    while x > 0:
        x //= 5
        y += x
    return y
 
num = 10
print("Factorial of",num,"is",
factorial(num),"and Have last 0 is",factendzero(num))

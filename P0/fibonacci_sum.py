def fib(n):
    a, b = 0, 1
    contador = 0
    while a < n:
        contador += a
        a, b = b, a+b
    return contador


def fib_sum(m):
    sumation = 0
    for elem in fib(m):
        sumation += elem
    return sumation


number = int(input("Please enter an inteer: "))
print(fib_sum(number))

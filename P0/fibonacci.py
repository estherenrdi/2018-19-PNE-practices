def fib(n):
    a, b = 0,1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
m = int(input("Ingresa límite máximo de la sucesión: "))
fib(m)


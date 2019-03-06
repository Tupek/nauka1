def fib(n):
    a, b = 0, 1
    for i in range(0, n):
        yield a
        a, b = b, a + b

for element in fib(5):
    print(element)
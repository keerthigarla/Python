def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
def fib_pos(n1):
    lst=[]
    for i in range(8):
        lst.append(fibonacci(i))
    return print(lst[n1])
fib_pos(6)

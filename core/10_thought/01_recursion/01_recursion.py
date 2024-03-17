def climbStairs(n):
    # a, b = 1, 2
    # for _ in range(n-1):
    #     a, b = b, a+b
    # return a

    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return climbStairs(n-1) + climbStairs(n-2)


def fib(n):
    # a, b = 0, 1
    # for _ in range(n):
    #     a, b = b, a+b
    # return a

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)


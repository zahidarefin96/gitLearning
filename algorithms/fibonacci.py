
# O(n)
def fibonacci(n):
    if n < 0:
        return 'Not a valid number'
    if n == 0:
        return 0
    # if n == 1:
    #     return [1]
    # if n == 2:
    #     return [1, 1]

    index = 3
    fib_1 = 1
    fib_2 = 1
    # index = 6, n = 5 fib_1 = 1, fib_2 = 1
    # result = [1, 1, 2, 3, 5]
    result = [fib_1, fib_2]

    while index <= n:
        result.append(fib_1 + fib_2)
        fib_1, fib_2 = fib_2, fib_1 + fib_2
        index = index + 1  # index += 1

    return result


n = 5
print(n)
print(fibonacci(n))

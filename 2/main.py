# 2479
def f(n, c):
    if n > c or n == 10:
        return 0
    if n == c:
        return 1
    if n < c:
        return f(n + 1, c) + f(n + 2, c) + f(n * 2, c)


print(f(2, 12))

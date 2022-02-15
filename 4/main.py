# 450
def f(n, c):
    if n > c or n == 22:
        return 0
    if n == c:
        return 1
    if n < c:
        return f(n + 1, c) + f(n * 2, c)


print(f(2, 15) * f(15, 31))

# 3088
def f(n, c):
    if n > c:
        return 0
    if n == c:
        return 1
    if n < c:
        return f(n + 1, c) + f(n + 2, c)


print(f(5, 10) * f(10, 15))
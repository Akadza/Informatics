# 3445
def f(n, c, z):
    if n > c or z > 6:
        return 0
    if n == c:
        return 1
    if n < c:
        return f(n + 1, c, z + 1) + f(n + 5, c, z + 1) + f(n * 3, c, z + 1)


print(f(1, 111, 0))



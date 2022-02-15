# 2764
def f(n, c, z):
    global count
    if n > c:
        return 0
    if n == c:
        if z == 8:
            count += 1
        return 1
    if n < c:
        return f(n + 1, c, z + 1) + f(n * 2, c, z + 1) + f(n * 3, c, z + 1)


count = 0
f(1, 34, 0)
print(count)
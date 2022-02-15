# 3452
def f(n, c):
    global kList
    if n > c:
        return 0
    if n == c:
        return 1
    if n < c:
        return f(n + 2, c) + f(n + 4, c) + f(n + 5, c)


for c in range(0, 6000):
    if f(31, c) == 1001:
        print(c)

# 3451
def f(n, c):
    global count
    if n > c:
        return 0
    if n == c:
        count = count + 1
        return 1
    if n < c:
        return f(n + 2, c) + f(n + 5, c)


count = 0
for c in range(5, 100):
    f(5, c)
    if count == 34:
        print(c)
    else:
        count = 0

# 467
def f(n, c):
    global count
    if n > c:
        return 0
    if n == c:
        return 1
    if n < c:
        if n + 1 == 31:
            count += 1
        return f(n + 1, c) + f(n * 2, c)



count = 0
print(f(5, 32))
print(count)


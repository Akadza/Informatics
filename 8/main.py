# 3710
# перевод в двоичную систему
def num2(n):
    result = ""
    while n != 0:
        result += str(n % 2)
        n = n // 2
    result = "".join(reversed(result))
    return int(result)


# перевод в десятичную
def num10(n):
    n = str(n)
    result = 0
    for i in range(len(n)):
        result += (int(n[i]) * 2**(len(n) - 1 - i))
    return result


def f(n, c):
    if n > c:
        return 0
    if n == c:
        return 1
    if n < c:
        return f(num2(num10(n) + 1), c) + f(int(str(n) + "0"), c) + f(int(str(n) + "1"), c)


print(f(101, 101110))

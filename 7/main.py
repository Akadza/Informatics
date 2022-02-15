# 3575 Решу ЕГЭ
def f(n, z):
    global nums
    if z > 4:
        return 0
    if z == 4:
        nums.add(n)
        return 1
    if z < 4:
        f(n * 5, z + 1)
        f(n * 3, z + 1)


nums = set()
f(81, 0)
print(len(nums))





def f(n):
    if 0 < n < 10:
        return True
    return False


def g(n):
    if n % 3 == 0:
        return True
    return False


s = 0
while True:
    a = int(input())
    if a == 0:
        print(s)
        break
    if f(a) and g(a):
        s += a

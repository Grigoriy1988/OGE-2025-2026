def f(n):
    if n % 2 == 0:
        return True
    return False


def g(n):
    if n % 9 == 0:
        return True
    return False


count = 0
while True:
    a = abs(int(input()))
    if a == 0:
        print(count)
        break
    if f(a) and g(a):
        count += 1

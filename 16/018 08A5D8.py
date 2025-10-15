def f(x):
    if abs(x) % 4 == 0 or abs(x) % 9 == 0:
        num.append(x)

num = []
while True:
    a = int(input())
    f(a)
    if a == 0:
        print(sum(num) if num else 0)
        break

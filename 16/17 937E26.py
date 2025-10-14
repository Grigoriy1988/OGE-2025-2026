def f(lst):
    if lst:
        print(sum(lst)/len(lst))
    else:
        print('NO')

def g(x):
    if 100<=x<=999:
        num.append(x)

num = []
while True:
    a = int(input())
    if a == 0:
        f(num)
        break
    g(a)
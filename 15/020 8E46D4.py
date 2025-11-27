def f(x):
    if x > 0:
        s.append(x)
s = []
n = int(input())
for _ in range(n):
    f(int(input()))
print(sum(s) / len(s))
print(len(s))


    
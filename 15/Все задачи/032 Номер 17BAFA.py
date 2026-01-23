s = 0
n = int(input())
for _ in range(n):
    a = int(input())
    if a % 5 == 0:
        s += a
print(s)


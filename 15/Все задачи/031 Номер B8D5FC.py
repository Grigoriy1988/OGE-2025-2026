s = 0
n = int(input())
for _ in range(n):
    a = int(input())
    if a % 3 == 0 and a % 10 == 8:
        s += a
print(s)


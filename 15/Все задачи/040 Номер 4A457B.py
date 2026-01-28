m = 30002
n = int(input())
for _ in range(n):
    a = int(input())
    if a % 10 == 2 and m > a:
        m = a
print(m)


m = 30006
n = int(input())
for _ in range(n):
    a = int(input())
    if a % 10 == 6 and m > a:
        m = a
print(m)


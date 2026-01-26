s = 0
while True:
    a = int(input())
    if a == 0:
        break
    if a % 4 == 0 and 100 <= a <= 999:
        s += a
print(s)

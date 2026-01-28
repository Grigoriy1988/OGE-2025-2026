s = 0
count = 0
while True:
    a = int(input())
    if a == 0:
        break
    if 10 <= a <= 99:
        s += a
        count += 1
print(s / count if count else "NO")

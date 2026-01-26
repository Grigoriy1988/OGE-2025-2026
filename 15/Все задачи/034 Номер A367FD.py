s = 0
count = 0
n = int(input())
for _ in range(n):
    t = int(input())
    s += t
    if t > 0:
        count += 1
print(s / n, '\nYES' if count >= 5 else '\nNO')

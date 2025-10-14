s = 0
count = 0
while True:
    a = int(input())
    if a == 0:
        print("NO" if count == 0 else s / count)
        break
    elif 10 <= a <= 99:
        s += a
        count += 1

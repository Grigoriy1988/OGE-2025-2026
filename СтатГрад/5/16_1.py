count = 0
while True:
    a = int(input())
    if a == 0:
        print(count)
        break
    if a % 4 == 0 and a % 10 == 2:
        count += 1

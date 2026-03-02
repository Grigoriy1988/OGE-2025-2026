count = 0
while True:
    a = int(input())
    if a == 0:
        print(count)
        break
    if a % 8 == 2 and int('100', 8) <= a <= int('777', 8):
        count += 1

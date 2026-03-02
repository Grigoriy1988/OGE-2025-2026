count = 0
while True:
    a = int(input())
    if a == 0:
        print(count)
        break
    if a % 16 == 8 and int('100', 16) <= a <= int('FFF', 16):
        count += 1

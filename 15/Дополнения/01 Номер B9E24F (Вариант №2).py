count = 0
count2 = 0
while True:
    a = int(input())
    if a == 0:
        print(count)
        print(count2)
        break
    if a % 16 == 13 and int('100', 16) <= a <= int('FFF', 16):
        count += 1
    if a % 16 == 13 and 1 * 16 ** 2 + 0 * 16 ** 1 + 0 * 16 ** 0 <= a <= 15 * 16 ** 2 + 15 * 16 ** 1 + 15 * 16 ** 0:
        count2 += 1

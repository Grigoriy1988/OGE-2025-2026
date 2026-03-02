count = 0
for _ in range(int(input())):
    a = int(input())
    if a % 16 == 9 and int('100', 16) <= a <= int('FFF', 16):
        count += 1
print(count)
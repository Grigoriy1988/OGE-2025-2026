count = 0
for _ in range(int(input())):
    a = int(input())
    if a % 8 == 4 and int('1000', 8) <= a <= int('7777', 8):
        count += 1
print(count)
count = 0
while True:
    a = int(input())
    if a == 0:
        print(count)
        break
    if a % 8 == 1 and int('1000', 8) <= a <= int('7777', 8):
        count += 1

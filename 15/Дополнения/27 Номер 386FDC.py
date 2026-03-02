count = 0
while True:
    a = int(input())
    if a == 0:
        print(count)
        break
    if a % 5 == 2 and int('1000', 5) <= a <= int('4444', 5):
        count += 1

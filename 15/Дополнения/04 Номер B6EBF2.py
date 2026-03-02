count = 0
while True:
    a = int(input())
    if a == 0:
        break
    if a % 5 == 0 and int('1000', 5) <= a <= int('4444', 5):
        count += 1
print(count)
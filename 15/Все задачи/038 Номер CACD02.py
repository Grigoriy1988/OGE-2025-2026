count = 0
while True:
    a = int(input())
    if a == 0:
        break
    if a % 3 == 0 and 1 <= a <= 9:
        count += 1
print(count)

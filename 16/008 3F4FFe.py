count = 0
while True:
    a = int(input())
    if a == 0:
        print(count)
        break
    elif a % 5 == 0 and a % 2 == 0:  # a % 10 == 0
        count += 1

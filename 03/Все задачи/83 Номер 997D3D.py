for x in range(999, 99, -1):
    if not (x // 100 % 2 != 0) and not (x % 3 == 0):
        print(x)
        break

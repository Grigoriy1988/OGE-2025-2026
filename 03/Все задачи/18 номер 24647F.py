for x in range(999, 99, -1):
    if not (x // 100 % 2 != 0) and  (x % 3 == 0):
        print(x)
        break
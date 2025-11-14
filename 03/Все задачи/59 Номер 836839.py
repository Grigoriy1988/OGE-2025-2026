for x in range(74, 9, -1):
    if ((x % 10 + x // 10) % 2 != 0) and not(x % 2 == 0):
        print(x)
        break

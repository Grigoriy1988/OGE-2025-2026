for x in range(125,99,-1):
    if (sum(int(i) for i in str(x)) % 5 == 0) and not(x % 2 == 0):
        print(x)
        break
        
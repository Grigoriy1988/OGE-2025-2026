for b in range(1,100):
    a = 1
    a *= 3 #1
    a += b #2
    a *= 3 #1
    a += b #2
    a *= 3 #1
    if a == 99:
        print(b)



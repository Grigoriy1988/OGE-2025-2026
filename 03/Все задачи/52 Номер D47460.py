a = [638, 442, 357, 123]
for x in a:
    if not (int(str(x)[0]) % 2 == 0) and (sum(int(i) for i in str(x)) % 2 == 0):
        print(x)

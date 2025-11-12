a = [638, 442, 357, 123]
for i in a:
    if not (i // 100 % 2 == 0) and not ((sum(int(j) for j in str(i))) % 2 == 0):
        print(i)
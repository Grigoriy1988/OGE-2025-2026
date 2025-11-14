a = [6843, 4562, 3561, 1234]
for x in a:
    if not (x // 1000 % 2 == 0 ) and not (x % 2 != 0):
        print(x)

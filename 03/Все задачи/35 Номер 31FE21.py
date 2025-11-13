a = [6843, 4562, 3561, 1234]
for i in a:
    if not (i // 1000 % 2 == 0) and  ( i % 10 % 2 != 0):
        print(i)
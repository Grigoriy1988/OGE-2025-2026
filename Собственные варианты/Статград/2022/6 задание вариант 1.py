list_k_s = [(10, 12), (8, -10), (16, 2), (5, -5), (-3, 9), (-10, 7), (-10, -2), (14, 1), (20, 5)]
for A in range(-100,90):
    count = 0
    for k,s in list_k_s:
        if (s > A) or (k > 9):
            pass
        else:
            count += 1
    if count == 4:
        print(f'A = {A}',end='; ')
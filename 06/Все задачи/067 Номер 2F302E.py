list_s_k = [(6, 6), (7, 1), (16, 10), (20, 2), (10, 3), (12, 2), (2, 2), (0, 6), (4, 5)]
count = 0
for s, k in list_s_k:
    if s % 6 == k:
        count += 1
        print("YES")
    else:
        print("NO")
print(f'Ответ: {count}')

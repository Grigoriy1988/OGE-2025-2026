list_s_k = [(1, 2), (5, 0), (18, 3), (21, 1), (10, 2), (12, 1), (9, 4), (5, 5), (3, 3)]
count = 0
for s, k in list_s_k:
    if s % 5 == k:
        count += 1
        print("YES")
    else:
        print("NO")
print(f'Ответ: {count}')

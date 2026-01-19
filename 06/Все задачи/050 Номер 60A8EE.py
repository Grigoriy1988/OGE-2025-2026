list_s_k = [(2, 2), (7, 0), (14, 10), (22, 1), (10, 3), (12, 1), (9, 2), (5, 1), (2, 5)]
count = 0
for s, k in list_s_k:
    if s % 7 == k:
        count += 1
        print("YES")
    else:
        print("NO")
print(f'Ответ: {count}')

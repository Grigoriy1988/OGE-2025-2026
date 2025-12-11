list_s_k = [(1, 1), (7, 0), (8, -12), (6, 6), (3, 11), (-10, -12), (10, 2), (7, 1), (12, 6)]
count = 0
for s, k in list_s_k:
    if s > 6 and k < 6:
        count += 1
        print("YES")
    else:
        print("NO")
print(f'Ответ: {count}')

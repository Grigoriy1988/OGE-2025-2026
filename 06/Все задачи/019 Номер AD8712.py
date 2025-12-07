list_s_k = [(9, 0), (10, 10), (18, 9), (22, 4), (27, 3), (12, 9), (29, 2), (4, 2), (3, 3)]
count = 0
for s, k in list_s_k:
    if s % 9 == k:
       print("YES")
       count += 1
    else:
        print("NO")
print(f'Ответ: {count}')


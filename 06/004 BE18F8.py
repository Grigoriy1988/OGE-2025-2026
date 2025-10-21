list_s_t = [(12, 5), (5, 3), (-4, 1), (2, -5), (5, -7), (10, 3), (18, 6), (3, 0), (2, 5)]
count = 0
for s,t in list_s_t:
    if not ((s >= 2) and (t < 5)):
        print("YES")
        count += 1
    else:
        print("NO")
print(f'ответ: {count}')


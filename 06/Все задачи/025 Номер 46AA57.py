list_s_t = [(2, 5), (-2, 4), (4, 1), (-11, -5), (3, -7), (1, 8), (8, 2), (3, 0), (23, 1)]
count = 0
for s, t in list_s_t:
    if (s < -2) or not (t < 4):
        print("YES")
        count += 1
    else:
        print("NO")

print(f'Ответ: {count}')

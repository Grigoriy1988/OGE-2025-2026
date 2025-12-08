list_s_k = [(3, 6), (6, 3), (-3, 3), (3, -3), (-10, -10), (10, 10), (-7, 7), (8, -10), (5, 8)]
count = 0
for s, k in list_s_k:
    if s < 4 or k < 7:
        print("ДА")
    else:
        count += 1
        print("НЕТ")
print(f'Ответ:{count}')

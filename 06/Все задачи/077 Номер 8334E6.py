list_s_t = [(-9, 11), (2, 7), (5, 12), (2, -2), (7, -9), (12, 6), (9, -1), (7, 11), (11, -5)]
list_A = []
for A in range(-100, 100):
    count = 0
    for s, t in list_s_t:
        if(s > A) or (t > 11):
            count += 1
            # print("YES")
        else:
            pass
            #print("NO")

    if count == 4:
        list_A.append(A)
print(f'Ответ: {min(list_A)}')

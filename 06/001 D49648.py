list_s_t = [(13, 2), (11, 12),(-12, 12), (2,-2), (-10,-10), (6,-5), (2, 8), (9, 10), (1, 13)]
for A in range(-1200, 1300):
    count = 0
    for s,t in list_s_t:
        if (s>A) or (t > 12):
            continue #print("YES")
        else:
            count += 1 #print("NO")
    if count == 5:
        print(A)



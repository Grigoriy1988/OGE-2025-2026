list_s_t = [(1, 2), (11, 2), (1, 12), (11, 12), (-11,-12),(-11, 12),(-12, 11),(10, 10), (10, 5)]
for A in range(-1200, 1100):
    count = 0
    for s,t in list_s_t:
        if (s > 10) or (t > A):
            continue #print("YES")
        else:
            count += 1 #print("NO")
    if count == 5:
        print(A)



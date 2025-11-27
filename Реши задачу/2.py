n = 6
inf = 30_000
w = [[0, 2, 4, inf, inf, inf],
     [2, 0, 9, 7, inf, inf],
     [4, 9, 0, 8, 1, inf],
     [inf, 7, 8, 0, 3, 1],
     [inf, inf, 1, 3, 0, 2],
     [inf, inf, inf, 1, 2, 0]
     ]
col = [i for i in range(n)]
ostov = []
for k in range(n - 1):
    minDist = 1e10
    for i in range(n):
        for j in range(n):
            if col[i] != col[j] and w[i][j] < minDist:
                iMin = i
                jMin = j
                minDist = w[i][j]
    ostov.append((iMin, jMin))
    c = col[jMin]
    for i in range(n):
        if col[i] == c:
            col[i] = col[iMin]
for edge in ostov:
    print('(',edge[0],',',edge[1],')')
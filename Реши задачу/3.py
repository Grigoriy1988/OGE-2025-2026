n = 6
inf = 30_000
w = [[0, 2, 4, inf, inf, inf],
     [2, 0, 9, 7, inf, inf],
     [4, 9, 0, 8, 1, inf],
     [inf, 7, 8, 0, 3, 1],
     [inf, inf, 1, 3, 0, 2],
     [inf, inf, inf, 1, 2, 0]
     ]
selected = [False] * n
dist = [inf] * n
start = 0
dist[0] = 0
v = start
minDist = 0
while minDist < inf:
    selected[v] = True
    for j in range(n):
        if dist[v] + w[v][j] < dist[j]:
            dist[j] = dist[v] + w[v][j]
    minDist =1e10
    for j in range(n):
        if not selected[j] and dist[j] < minDist:
            minDist =dist[j]
            v = j
v = n - 1
print(v)
while v != start:
    for i in range(n):
        if i != v and dist[i] + w[i][v] == dist[v]:
            v = i
    break
print(v)
print(dist)
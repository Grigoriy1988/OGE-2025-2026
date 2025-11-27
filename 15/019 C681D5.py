n = int(input())
temp = []
for _ in range(n):
    temp.append(int(input()))
m = min(temp)
print(m)
print('Yes' if m < -15 else 'No')

from random import shuffle
s = input().split('\t')
n = int(input())
for i in range(n):
    shuffle(s)
print('\n'.join(s))
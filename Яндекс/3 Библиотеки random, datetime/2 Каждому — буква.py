from random import sample

s = list(set(input()))
print(''.join(sample(s, k=int(input()))))

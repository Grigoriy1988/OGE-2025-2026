list_answer = []
n = int(input())
for _ in range(n):
    a = int(input())
    if a % 2 == 0:
        list_answer.append(a)
print(min(list_answer))


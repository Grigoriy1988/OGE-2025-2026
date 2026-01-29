list_answer = []
n = int(input())
for _ in range(n):
    a = int(input())
    if a % 3 == 0:
        list_answer.append(a)
print(sum(list_answer))


list_answer = []
n = int(input())
for _ in range(n):
    a = int(input())
    if a % 10 == 2:
        list_answer.append(a)
print(max(list_answer))

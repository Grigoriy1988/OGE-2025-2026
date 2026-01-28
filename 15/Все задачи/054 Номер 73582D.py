list_answer = []
n = int(input())
for _ in range(n):
    a = int(input())
    if a % 10 == 3:
        list_answer.append(a)
print(len(list_answer))


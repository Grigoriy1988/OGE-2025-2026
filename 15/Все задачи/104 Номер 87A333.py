list_answer = []
n = int(input())
for _ in range(n):
    a = int(input())
    if a >= 8:
        list_answer.append(a)
print(len(list_answer))
print(sum(list_answer) / len(list_answer))


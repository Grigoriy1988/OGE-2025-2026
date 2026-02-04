list_answer = []
n = int(input())
for _ in range(n):
    a = int(input())
    if a % 10 == 5:
        list_answer.append(a)
print(sum(list_answer))


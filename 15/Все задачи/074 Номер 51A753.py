list_answer = []
n = int(input())
for _ in range(n):
    a = int(input())
    if a % 3 == 0 and a % 10 == 8:
        list_answer.append(a)
print(len(list_answer))


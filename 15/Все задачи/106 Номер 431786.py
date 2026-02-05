list_answer = []
while True:
    a = int(input())
    if a == 0:
        break
    if a % 10 == 1:
        list_answer.append(a)
print(sum(list_answer) / len(list_answer) if list_answer else "NO")


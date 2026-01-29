list_answer = []
while True:
    a = int(input())
    if a == 0:
        break
    if a % 3 == 0:
        list_answer.append(a)
print(min(list_answer))


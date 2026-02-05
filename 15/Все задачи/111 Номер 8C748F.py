list_answer = []
while True:
    a = int(input())
    if a == 0:
        break
    if a % 10 == 2 and a % 4 == 0:
        list_answer.append(a)
print(len(list_answer))


list_answer = []
while True:
    a = int(input())
    if a == 0:
        break
    if a % 5 == 0 or a % 7 == 0:
        list_answer.append(a)
print(len(list_answer))


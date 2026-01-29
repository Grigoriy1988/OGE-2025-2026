list_answer = []
while True:
    a = int(input())
    if a == 0:
        break
    if a % 10 == 0 and a % 7 == 0:
        list_answer.append(a)
print(sum(list_answer))


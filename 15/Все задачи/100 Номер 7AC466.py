list_answer = []
while True:
    a = int(input())
    if a == 0:
        break
    if a % 6 == 0 and a % 10 == 4:
        list_answer.append(a)
print(sum(list_answer))


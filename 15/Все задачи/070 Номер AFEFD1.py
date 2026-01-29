list_answer = []
while True:
    a = int(input())
    if a == 0:
        break
    if a % 6 == 0 or a % 11 == 0:
        list_answer.append(a)
print(sum(list_answer))


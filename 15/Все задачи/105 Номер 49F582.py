list_answer = []
while True:
    a = int(input())
    if a == 0:
        break
    if a % 4 == 0 and 100 <= a <= 1000:
        list_answer.append(a)
print(len(list_answer))


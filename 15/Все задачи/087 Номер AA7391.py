list_answer = []
while True:
    a = int(input())
    if a == 0:
        break
    if a % 8 == 0 and 10 <= a <= 99:
        list_answer.append(a)
print(sum(list_answer))


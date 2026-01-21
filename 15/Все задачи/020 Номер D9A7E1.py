elements = []
while True:
    a = int(input())
    if a == 0:
        break
    if (a % 9) == 1:
        elements.append(a)
print(max(elements) if elements else "NO")


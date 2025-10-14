n = int(input())
numbers = []
for _ in range(n):
    a = int(input())
    if a % 10 == 4:
        numbers.append(a)
print(min(numbers))

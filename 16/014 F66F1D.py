def f(n):
    if n % 3 == 0 and n % 10 == 2:
        numbers.append(n)


numbers = []
n = int(input())
for _ in range(n):
    f(int(input()))
print(len(numbers))

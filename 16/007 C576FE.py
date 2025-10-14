# Решение на основе списков
numbers = []
while True:
    a = int(input())
    if a == 0:
        break
    numbers.append(a)
numbers_5_or_9 = [i for i in numbers if i % 5 == 0 or i % 9 == 0]
print(len(numbers_5_or_9))

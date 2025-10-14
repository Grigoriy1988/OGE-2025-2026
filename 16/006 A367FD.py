# Решение на основе списков
temperature = []
for _ in range(int(input())):
    temperature.append(int(input()))
print(sum(temperature) / len(temperature))
count = len([i for i in temperature if i > 0])
print("YES" if count > 5 else "NO")

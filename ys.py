from collections import Counter

game = []
for _ in range(int(input())):
    s = input().split(': ')
    s = s[1].split(', ')
    game.extend(s)
count = dict(Counter(game))
count = dict(sorted(count.items(), key=lambda item: (item[1], item[0]), reverse=True))
for key, value in count.items():
    print(f"{key} -> {value}")

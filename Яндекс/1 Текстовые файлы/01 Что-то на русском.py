with open('wises.txt', mode='r', encoding='utf-8') as f:
    n = int(input())
    thoughts = f.readlines()
    # print(thoughts)
    if n - 1 > len(thoughts):
        print('Мудрости закончились.')
    else:
        print(thoughts[n - 1])

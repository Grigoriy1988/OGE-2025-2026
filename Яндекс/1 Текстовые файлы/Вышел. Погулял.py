with open('poem.txt', mode='r', encoding='utf-8') as r, open('counting.txt', mode='w', encoding='utf-8') as w:
    for i, line in enumerate(r.readlines(), start=1):
        print(f'{i} - {line.rstrip()}', file=w)

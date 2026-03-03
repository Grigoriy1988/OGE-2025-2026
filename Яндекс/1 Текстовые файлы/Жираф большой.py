with open('giraffe_equation.txt', mode='w', encoding='utf-8') as f:
    line = ''
    m = 0
    for _ in range(int(input())):
        s = input()
        m = max(len(s), m)
        line += s
    for i in range(0, len(line), m):
        print(line[i:i + m], file=f)
        
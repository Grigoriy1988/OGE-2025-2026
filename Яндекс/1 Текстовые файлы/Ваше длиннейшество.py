with open('line.txt', mode='r', encoding='utf-8') as r:
    line = r.readline()
    m = 0
    long = 0
    for i in line:
        if i == 'S' and long == 0:
            long = 1
        elif i == 'S' and long != 0:
            long += 1
        else:
            m = max(m, long)
            long = 0
m = max(m, long)
print(m)

with open('data.bin', mode='rb') as r, open('part.dat', mode='wb') as w:
    data = r.read(100)
    w.write(data)

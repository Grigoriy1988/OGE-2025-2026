x = - 10000
print(x)
a = []
while x <= 100:
    if abs(9 ** x + 12 ** x - 16 ** x) <= 0.001:
        print(f"при {x} {9 ** x + 12 ** x - 16 ** x}")
        a.append((9 ** x + 12 ** x - 16 ** x,x))


    x+= 1
print(min(a))
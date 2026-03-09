count = 0
while True:
    a = int(input())
    if a == 0:
        print(count)
        break
    h = hex(a)[2:]
    if len(h) == 3 and h[-1] == 'd':
        count += 1
"""
Плохой способ решения так как подходит только под базовые системы счисления:
hex - шестнадцатеричная
oct - восьмеричная
bin - двоичная 
"""
digit = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def f(number ,radix):
    answer = 0
    i = 0
    for dig in number[::-1].upper():
        answer += digit.index(dig) * radix**i
        i += 1
    return answer

a = f('110001',2)
print(f"110001 в двоичной системе это {a} в десятичной")


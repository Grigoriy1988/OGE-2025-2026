# Программа перевод из десятичной системы счисления в систему
# с произвольным основанием (≤36):
digit = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def f(number,radix):
    answer = ''
    while number > 0:
        answer = digit[number % radix] +answer
        number //= radix
    return answer

print(f(126,16))


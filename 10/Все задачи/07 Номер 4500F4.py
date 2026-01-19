dig  = '0123456789ABCDEF'
def f(number,radix):
    answer = ''
    while number > 0:
        answer = dig[number % radix] + answer
        number //= radix
    return answer


n = int(input("Введите число в десятичной системе счисление "))
r = int(input("Введите новое основание "))
print(f'{n} = {f(n,r)}')
print(f'{f(n,r).count('1')} единиц в числе')
print(f'{f(n,r).count('0')} нулей в числе')

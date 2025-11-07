digit = '01'
def f(number,radix):
    answer = ''
    while number > 0:
        answer = digit[number % radix] +answer
        number //= radix
    return answer

print(f'62 => {f(62,2)} => {f(62,2).count('1')} ед.')
print(f'71 => {f(71,2)} => {f(71,2).count('1')} ед.')
print(f'74 => {f(74,2)} => {f(74,2).count('1')} ед.')

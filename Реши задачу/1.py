# Шифр Цезаря
s1 = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
s2 = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'.lower()
message  = input('Введите строку для шифрования:\n>> ')
k = int(input('Введите величину сдвига:\n>> '))
code = ''
for symbol in message:
    if symbol in s1:
        code += s1[(s1.index(symbol) + k) % 33]
    elif symbol in s2:
        code += s2[(s2.index(symbol) + k) % 33]
    else:
        code += symbol
print(f'Зашифрованное послание: {code}')
input()

i, unit = input('Информационный вес одного символа (пример: 1 байт)\n').lower().split()
if unit == 'бит':
    i = int(i)
elif unit == 'байт':
    i = int(i) * 8
words = [word for word in input('Введите текст:\n').split()]
i2, unit = input('На сколько текст стал меньше (пример: 1 байт)\n').lower().split()
if unit == 'бит':
    i2 = int(i2)
elif unit == 'байт':
    i2 = int(i2) * 8
for word in words:
    if (len(word) + 1) * i == i2:
        print(f'Возможное слово "{word[:-1]}"')

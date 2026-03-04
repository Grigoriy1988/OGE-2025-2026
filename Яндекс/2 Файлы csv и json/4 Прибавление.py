import json

with open("animals.json", encoding="utf-8") as f:
    data = json.load(f)  # Превращаем JSON в словарь или спис
    # print(data)
    # print(data['white hare'])
    # print(type(data))
    m = 0
    for i in data.values():
        m = max(m, i[1] - i[0])
    for i in data:
        if data[i][1] - data[i][0] == m:
            print(i)
        # if (i[1] - i[0]) == m:
        #     print()

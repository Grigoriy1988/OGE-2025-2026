import json

with open("placeholder.json", 'w', encoding="utf-8") as f:
    word = input().upper()
    w = {}
    for i in range(0, len(word)):
        w[word[i]] = i
    # print(w)
    json.dump(w, f)


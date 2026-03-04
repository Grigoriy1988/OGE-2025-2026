import csv
import json

out = []
with open("weather.csv", encoding="utf-8") as f:
    reader = list(csv.DictReader(f, delimiter="|"))
    for i in range(0, len(reader)):
        # print(reader[i])
        for j in range(i, len(reader)):
            if int(reader[i]["temperature"]) < int(reader[j]["temperature"]):
                t = (j - i)
                break
        else:
            t = 0

        out.append({"date": reader[i]['date'], "temperature": int(reader[i]["temperature"]), "warming": t})
with open("warming.jsonl", 'w', encoding="utf-8") as output:
    for line in out:
        output.write(json.dumps(line) + '\n')

import csv
import json
from datetime import datetime

with open("wake_up.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f, delimiter=";")
    d = {}
    for row in reader:
        t = datetime.strptime(f'{str(row["date"]} {row['woke_time']}', '%Y/%m/%d %M:%H')

        if row["name"] not in d or t < d[row["name"]]:
            d[row['name']] = (row['date'], t )






    print(d)
# with open("early.json", 'w', encoding="utf-8") as output:
#     json.dump(d, output, ensure_ascii=False, indent=4)

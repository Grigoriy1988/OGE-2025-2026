import csv

with open("beaches.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f, delimiter=";")
    for row in reader:
        if row['equipped'] == "1" and row['rescuers'] == '1' and float(row['pollution']) <= 0.5 and float(
                row['temperature']) > 18:
            print(row['beach'])

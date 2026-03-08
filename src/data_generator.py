import random
import csv

rows = []

for i in range(2000):

    voltage = round(random.uniform(4.7,5.3),2)
    current = round(random.uniform(0.1,0.6),2)
    temperature = random.randint(25,70)
    time = random.randint(10,50)

    result = "PASS"

    if voltage < 4.9 or current > 0.45 or temperature > 55:
        result = "FAIL"

    rows.append([voltage,current,temperature,time,result])


with open("data/pcb_test_data.csv","w",newline="") as f:

    writer = csv.writer(f)

    writer.writerow([
        "voltage",
        "current",
        "temperature",
        "time",
        "result"
    ])

    writer.writerows(rows)

print("Dataset generated")
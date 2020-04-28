import csv

l = []
with open ("final_test.csv", 'r') as f:
    with open("pokemon_list.csv", "w+") as out_file:
        writer=csv.writer(out_file)
        for row in csv.reader(f):
            if any(row):
                writer.writerow(row)
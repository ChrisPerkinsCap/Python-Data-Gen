import csv

source_dir = "/Users/chris/Dev/Python-Data-Gen/CSV/"

FirstNames = []

with open(source_dir + "FirstNames-fr.csv", mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'{row["name"]}\t\t{row["sex"]}\t\t{row["NameCount"]}\t\t{row["Rand"]}')
            line_count += 1
    print(f'Processed {line_count} lines.')
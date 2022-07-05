import csv
f = open('data.csv','r')
obj = csv.reader(f)

for line in obj:
    print(type(line))
f.close()
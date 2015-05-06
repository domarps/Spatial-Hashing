import csv
import sys

f = open(sys.argv[1], 'rt')
try:
    csv_object = csv.reader(f)
    text = []
    XCoord = []
    YCoord = []
    for row in csv_object:
        text.append(row[0])
        XCoord.append(row[1])
        YCoord.append(row[2])
finally:
    f.close()
print len(text)
print len(XCoord)
print len(YCoord)

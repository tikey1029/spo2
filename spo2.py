import numpy as np
import csv

data_lists = np.loadtxt('zq2.csv')

dataset = []
for data in data_lists:
    dataset.append(data)

dataset = np.array(dataset)
dataset2 = (dataset.ravel()[np.flatnonzero(dataset)])

a = 0
b = 0
c = 0
i = 0
j = 0
for data in dataset2:
    if data >= 95:
        a += 1
        if data == 99:
            i += 1
        elif data == 97:
            j += 1
    elif 90 <= data <= 94:
        b += 1
    elif 85 <= data <= 89:
        c += 1

x = len(dataset2)

np.savetxt('rzq2.csv', dataset2)

f = open('rzq2.csv', 'a+', encoding = 'utf-8', newline = '')
csv_writer = csv.writer(f)

csv_writer.writerow([" "," "])
csv_writer.writerow(["spO2","百分比"])
csv_writer.writerow(["99",'{:.2%}'.format(i/x)])
csv_writer.writerow(["95以上",'{:.2%}'.format(a/x)])
csv_writer.writerow(["90~94：",'{:.2%}'.format(b/x)])
csv_writer.writerow(["85~89：",'{:.2%}'.format(c/x)])
csv_writer.writerow(["97：",'{:.2%}'.format(j/x)])
csv_writer.writerow(["总记录点数", x])

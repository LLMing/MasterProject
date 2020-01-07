import csv
import os
import numpy as np
import matplotlib.pyplot as plt

csvFile_task = csv.reader(open('result-address-new.csv', 'r'))

fileName = []

top_1 = []
top_2 = []
top_3 = []
top_4 = []
top_5 = []

guideline = {}

for item in csvFile_task:
    if len(item) >= 6 and item[4] != "id":
        fileName.append(item[4])

for fn in fileName:
    filepath = fn + ".csv"
    localpath = os.path.join('./result-csv', filepath)
    csvFile = csv.reader(open(localpath, 'r'))
    i, j, k, o, p = 0,0,0,0,0
    for item in csvFile:
        if item[0] == "WCAG2AAA.Principle1.Guideline1_4.1_4_6.G17.Fail" and item[2] != "notice" and item[2] != "warning":
            i += 1
        if item[0] == "WCAG2AAA.Principle4.Guideline4_1.4_1_2.H91.A.EmptyNoId" and item[2] != "notice" and item[2] != "warning":
            j += 1
        if item[0] == "WCAG2AAA.Principle4.Guideline4_1.4_1_1.F77" and item[2] != "notice" and item[2] != "warning":
            k += 1
        if item[0] == "WCAG2AAA.Principle1.Guideline1_1.1_1_1.H37" and item[2] != "notice" and item[2] != "warning":
            o += 1
        if item[0] == "WCAG2AAA.Principle1.Guideline1_4.1_4_6.G18.Fail" and item[2] != "notice" and item[2] != "warning":
            p += 1
    top_1.append(i)
    top_2.append(j)
    top_3.append(k)
    top_4.append(o)
    top_5.append(p)

max_1 = max(top_1)
min_1 = min(top_1)
average_1 = np.average(top_1)
median_1 = np.median(top_1)
percentile_1 = np.percentile(top_1, [25, 50, 75])
print("top_1", max_1, min_1, average_1, percentile_1)
print("top_2", max(top_2), min(top_2), np.average(top_2), np.percentile(top_2, [25, 50, 75]))
print("top_3", max(top_3), min(top_3), np.average(top_3), np.percentile(top_3, [25, 50, 75]))
print("top_4", max(top_4), min(top_4), np.average(top_4), np.percentile(top_4, [25, 50, 75]))
print("top_5", max(top_5), min(top_5), np.average(top_5), np.percentile(top_5, [25, 50, 75]))

labels = ["G17.Fail", "H91.A.EmptyNoId", "F77", "H37", "G18.Fail"]
plt.boxplot([top_1, top_2, top_3, top_4, top_5],labels=labels,showfliers=False,sym="o")
plt.show()

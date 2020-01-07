import csv
import os

csvFile_task = csv.reader(open('result-address-new.csv','r'))

fileName = []

guideline = {}

for item in csvFile_task:
    if len(item) >= 6 and item[4] != "id":
        fileName.append(item[4])

for fn in fileName:
    filepath = fn + ".csv"
    localpath = os.path.join('./result-csv', filepath)
    csvFile = csv.reader(open(localpath, 'r'))
    for item in csvFile:
        if item[0] != "code" and item[2] != "notice":
            if item[0] not in guideline:
                guideline[item[0]] = 1
            else:
                guideline[item[0]] += 1
fileHeader = ["code","number"]
newcsvFile = open('result-guideline-1.csv', 'w')
writer = csv.writer(newcsvFile)

writer.writerow(fileHeader)

for item in guideline:
    result = []
    result.append(item)
    result.append(guideline[item])
    writer.writerow(result)

newcsvFile.close()

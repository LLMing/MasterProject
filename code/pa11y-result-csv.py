import json
import csv

jsonFile = json.loads(open('combin.json').read())

csvFile = csv.reader(open('result.csv', 'r'))

resultJsonFile = json.loads(open('pa11y-result.json').read())
nameJsonFile = json.loads(open('pa11y-id-copy.json').read())

result = []
fileHeader = ['name', 'url', 'standard', 'address', 'id', 'result(total)', 'result(error)','result(warning)','result(notice)']
newcsvFile = open('result-address-new.csv', 'w')
writer = csv.writer(newcsvFile)

writer.writerow(fileHeader)

for item in csvFile:
    if csvFile.line_num != 1:
        if item[0] in jsonFile.keys():
            # print(item[0])
            item.append(jsonFile[item[0]])
        for aa in range(len(nameJsonFile)):
            model_str = nameJsonFile[aa]
            if model_str['name'] == item[0]:
                item.append(model_str['id'])
        if len(item) == 5:
            for bb in range(len(resultJsonFile)):
                model_dic = resultJsonFile[bb]
                if model_dic['task'] == item[4]:
                    item.append(model_dic['count']['total'])
                    item.append(model_dic['count']['error'])
                    item.append(model_dic['count']['warning'])
                    item.append(model_dic['count']['notice'])
                    break
        writer.writerow(item)
        print(item)
newcsvFile.close()

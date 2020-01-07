import json

resultJsonFile = json.loads(open('pa11y-result.json').read())
nameJsonFile = json.loads(open('pa11y-id-copy.json').read())

for aa in range(len(resultJsonFile)):
    model_str = resultJsonFile[aa]
    for bb in range(len(nameJsonFile)):
        model_dic = nameJsonFile[bb]
        if model_str['id'] == model_dic['id']:
            model_str['name'] = model_dic['name']

import json

file = open('simple.json', 'r', encoding='utf-8')
s = json.load(file)
file.close()
abc = {}
i = 0
for key, value in s.items():
    if value == "Website address not added":
        i += 1
        print(key, value)
        print(i)
        continue
    else:
        abc[key] = value

finalReasult = json.dumps(abc, indent=2)

with open('finwebsite.json', 'w') as file1:
    file1.write(finalReasult)
    file.close()

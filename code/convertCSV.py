import json
import csv


def read_json(filename):
    a = json.loads(open(filename).read())
    return a


def write_csv(data, filename):
    with open(filename, 'w') as outfile:
        headers = ['name', 'url', 'standard']
        writer = csv.writer(outfile)
        writer.writerow(headers)
        for key, value in data.items():
            writer.writerow([key, value, 'WCAG2AAA'])


write_csv(read_json('finwebsite.json'), 'result.csv')

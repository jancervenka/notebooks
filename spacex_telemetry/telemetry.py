import json

def parse(path):
    datafile = open(path, 'r')
    data = datafile.read().split('\n')[0 : -1]

    return map(lambda x: json.loads(x), data)



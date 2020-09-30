import json

def read(filename):
    with open(filename) as fp:
        string = json.load(fp)
    return string
def write(filename, data):
    with open(filename, 'w') as fp:
        json.dump(data, fp)
    return True

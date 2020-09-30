def read(filename):
    with open(filename) as fp:
        string = fp.read()
    return string
def write(filename, string):
    with open(filename, 'a') as fp:
        fp.write(string)
    return True
def overwrite(filename, string):
    with open(filename, 'w') as fp:
        fp.write(string)
    return True


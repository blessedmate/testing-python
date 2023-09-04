import os


def read_from_file(filename):
    if not os.path.exists(filename):
        raise Exception("Bad file")
    f = open(filename, "r")
    line = f.readline()
    return line

import os

def rel_filepath(filename):
    return os.path.join(os.path.dirname(__file__), filename)

def data_filepath(filename):
    return rel_filepath("data/%s" % (filename,))


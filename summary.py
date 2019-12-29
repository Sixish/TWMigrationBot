_msgs = []

def clear():
    _msgs.clear()

def get():
    return ",".join(_msgs)

def put(msg):
    _msgs.append(msg)


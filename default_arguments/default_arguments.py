from os.path import realpath, join, dirname

class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

op_file = open('res.txt', 'w')
def print_from_stream(n, stream=None):
    if stream is None:
        stream = EvenStream()
    for _ in range(n):
        if n != 0:
            o = stream.get_next()
            print(o)
            op_file.write(str(o)+'\n')

input_file = join(dirname(realpath(__file__)), 'sample.txt')
ip_file = open(input_file)

queries = int(ip_file.readline())
for _ in range(queries):
    stream_name, n = ip_file.readline().split()
    n = int(n)
    if stream_name == "even":
        print_from_stream(n)
    else:
        print_from_stream(n, OddStream())

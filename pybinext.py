import re
import shutil


def unbin(line):
    def decode_binary(x):
        return x.group(1) + str(int(x.group(2), 2))

    return re.sub(r'(\W)0b([0-1]+)', decode_binary, line)


def translate(fname):
    out = open(fname + '_', 'w')
    for line in open(fname):
        out.write(unbin(line))
    out.close()
    shutil.move(fname + '_', fname)

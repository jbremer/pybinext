import re
import shutil
import subprocess
import sys


def unbin(line):
    def decode_binary(x):
        return x.group(1) + str(int(x.group(2), 2))

    arr = line.split('"')
    quoted = False
    for x in xrange(len(arr)):
        if quoted is False:
            arr[x] = re.sub(r'(\W|^)0b([0-1]+)', decode_binary, arr[x])
            quoted = True
        elif arr[x] and arr[x][-1] != '\\':
            quoted = False

    return '"'.join(arr)


def translate(fname):
    out = open(fname + '_', 'w')
    for line in open(fname):
        out.write(unbin(line))
    out.close()
    shutil.move(fname + '_', fname)


def handle_cmdline(path, args):
    for fname in args:
        if fname[-2:] == '.c':
            # make a backup of the original file
            shutil.copy(fname, fname + '.bck')

            # translate the file
            translate(fname)

    # compile it
    subprocess.call([path] + args)

    for fname in args:
        if fname[-2:] == '.c':
            # restore the original file
            shutil.move(fname + '.bck', fname)

if __name__ == '__main__':
    for line in open(sys.argv[1]):
        print unbin(line)

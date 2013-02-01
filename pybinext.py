import re
import shutil
import subprocess


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

#!/usr/bin/env python
import shutil
import sys
import subprocess
import pybinext

try:
    import pybinext_config
    CL_PATH = pybinext_config.CL_PATH
except:
    CL_PATH = 'cl'

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'Usage: %s <input> [arguments...]' % sys.argv[0]
        exit(0)

    fname = sys.argv[1]

    # make a backup of the original file
    shutil.copy(fname, fname + '.bck')

    # translate the file
    pybinext.translate(fname)

    # compile it
    subprocess.call([CL_PATH, fname] + sys.argv[2:])

    # remove the backup file
    shutil.move(fname + '.bck', fname)

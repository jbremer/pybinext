#!/usr/bin/env python
import sys
import pybinext

try:
    import pybinext_config
    GCC_PATH = pybinext_config.GCC_PATH
except:
    GCC_PATH = 'gcc'

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'Usage: %s <arguments...>' % sys.argv[0]
        exit(0)

    pybinext.handle_cmdline(GCC_PATH, sys.argv[1:])

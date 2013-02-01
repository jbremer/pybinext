#!/usr/bin/env python
import sys
import pybinext

try:
    import pybinext_config
    CL_PATH = pybinext_config.CL_PATH
except:
    CL_PATH = 'cl'

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'Usage: %s <arguments...>' % sys.argv[0]
        exit(0)

    pybinext.handle_cmdline(CL_PATH, sys.argv[1:])

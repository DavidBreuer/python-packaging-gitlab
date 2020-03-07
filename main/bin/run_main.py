#!/usr/bin/env python
"""Run package and say hello.

Usage
-----
run_main.py argument
"""

import sys
import warnings

import main
import main.stuff


if __name__ == '__main__':

    # get script arguments
    ARGS = sys.argv

    # check that only one argument is given
    if len(ARGS) != 2:
        warnings.warn('Exactly one argument needed!')
        sys.exit()
    ARG = ARGS[1]

    # print argument
    print('Running function with argument:', ARG)

    # say hello
    main.stuff.say_hello(ARG)

    # add linebreak
    print('')

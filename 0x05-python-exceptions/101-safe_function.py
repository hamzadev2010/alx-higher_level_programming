#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    try:
        val = fct(*args)
    except BaseException as e:
        val = None
        print("Exception: {}".format(e), file=sys.stderr)
    finally:
        return val

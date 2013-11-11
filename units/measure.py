import fractions as frac

import units

class Measure(object):
    def __init__(self, value, *args):
        self._value = value
        nargs = len(args)
        if nargs == 0:
            self._unit = units.Unitless()
        elif nargs == 1 and isinstance(args[0], units.Unit):
                self._unit = args[0]
        else:
            self._unit = units.Unit(*args)

def sqrt():
    pass

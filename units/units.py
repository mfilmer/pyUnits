# Numbers with units, makes doing math easy!
# or something like that...

import fractions as frac
from numbers import Number

import baseUnits

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

class Unit(object):
    def __init__(self,*args):
        self.__units = dict()
        for unit in args:
            if isBaseUnit(unit):
                pass
            elif len(unit) == 2:
                pass
            else:
                raise ValueError

# Functions to verify unit type
# Verify that the provided unit is a base unit
def isBaseUnit(unit):
    return isinstance(BaseUnit, unit) and unit is not BaseUnit
# Get the type of the unit
# ex: meter*kilogram -> distance*mass
def getUnitType(unit):
    if isBaseUnit(unit):
        pass
    else:
        pass
# Verify that provided units are of the same type
def areUnitsCompatible(unitA, unitB):
    pass

# Maybe how I will deal with more complicated units such as Joules (kg*m^2/s^2)
class CompositeUnit(object):
    __metaclass__ = Singelton

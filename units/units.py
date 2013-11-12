# Numbers with units, makes doing math easy!
# or something like that...

from fractions import Fraction
from numbers import Number

import baseUnits

##### Functions #####
def sqrt():
    pass
# Verify that the provided unit is a base unit
def isBaseUnit(unit):
    return isinstance(BaseUnit, unit) and \
    unit is not BaseUnit() and \
    unit is not unit.getType()()
# Get the type of the unit
# ex: meter*kilogram -> distance*mass
def getType(unit):
    if isBaseUnit(unit):
        return unit.getType()
    else:
        pass
# Verify that provided units are of the same type
def areUnitsCompatible(unitA, unitB):
    pass

##### Objects #####
# A combination of a unit and a value
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

# A unit composed of multiple units with varying powers
class Unit(object):
    def __init__(self,*args):
        self._units = dict()
        for unit in args:
            if isBaseUnit(unit):
                self._units = {unit.getType(): (unit, Fraction(1))}
            elif len(unit) == 2:
                type = unit[0].getType()
                if type in self._units:
                    pass
                else:
                    pass
            else:
                raise ValueError

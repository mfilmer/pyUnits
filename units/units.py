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
    return isinstance(unit, baseUnits.BaseUnit) and \
    unit is not baseUnits.BaseUnit() and \
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
        elif nargs == 1 and isinstance(args[0], Unit):
                self._unit = args[0]
        else:
            self._unit = Unit(*args)
	
	# Value and Unit extraction methods
	def getValue(self):
		return self._value
	def getUnit(self):
		return self._unit
	
	# Magic Methods
	def __mul__(self, other):
		return Measure.__rmul__(other, self)
	def __rmul__(self, other):
		if isinstance(other, Number):
			self._value *= Number
		elif isinstance(other, Measure):
			self._value *= other._value
			self._unit *= other._unit
		elif isinstance(other, baseUnits.BaseUnit) or isinstance(other, Unit):
			self._unit *= other
		else:
			return NotImplemented
		return self

# A unit composed of multiple units, each with varying powers
class Unit(object):
    def __init__(self,*args):
        self._units = dict()
        for unit in args:
            if isBaseUnit(unit):
                self._units = {unit.getType(): (unit, Fraction(1))}
            elif len(unit) == 2:
                type = unit[0].getType()
                if type in self._units:
                    # Will need to convert to the other type
					# But really... people shouldn't be providing
					# units like "kg*slug*meter*foot"... thats just silly
					pass
                else:
                    self._units[type] = (unit[0], Fraction(unit[1]))
            else:
                raise ValueError

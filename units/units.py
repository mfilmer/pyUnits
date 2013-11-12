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
    def __str__(self):
        return str(self._value) + ' ' + str(self._unit)
    
    def __mul__(self, other):
        return Measure.__rmul__(other, self)
    def __rmul__(self, other):
        if isinstance(other, Number):
            return Measure(self._value * Number, self._unit)
        elif isinstance(other, Measure):
            return Measure(self._value * other._value, self._unit * other._unit)
        elif isinstance(other, baseUnits.BaseUnit) or isinstance(other, Unit):
            return Measure(self._value, self._unit * other)
        else:
            return NotImplemented
        return self

# A unit composed of multiple units, each with varying powers
class Unit(object):
    def __init__(self,*args):
        self._units = dict()
        for inUnit in args:
            if isBaseUnit(inUnit):
                self._units = {inUnit.getType(): (inUnit, Fraction(1))}
            elif isinstance(inUnit, Unit):
                for type, (unit, power) in inUnit._units.iteritems():
                    if type not in self._units:
                        self._units[type] = (unit, power)
                    else:
                        # Deal with converting units
                        # Probably deal with this later...
                        pass
            elif len(inUnit) == 2:
                type = inUnit[0].getType()
                if type in self._units:
                    # Will need to convert to the other type
					# But really... people shouldn't be providing
					# units like "kg*slug*meter*foot"... that's just silly
					pass
                else:
                    self._units[type] = (inUnit[0], Fraction(inUnit[1]))
            else:
                raise ValueError
    
    def __str__(self):
        string = ""
        for unit, power in self._units.itervalues():
            string += unit.getAbbr() + '^(' + str(power) + ')*'
        return string[:-1]
    
    def __mul__(self, other):
        return Unit.__mul__(other, self)
    def __mul__(self, other):
        if isinstance(other, Number):
            return Measure(other, self)
        elif isinstance(other, Unit):
            return Unit(self, other)
        else:
            return NotImplemented

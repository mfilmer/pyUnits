# Numbers with units, makes doing math easy!
# or something like that...

from fractions import Fraction
from numbers import Number

import baseUnits

##### Functions #####
def sqrt():
    pass
# Get the type of the unit
# ex: meter*kilogram -> distance*mass
def getType(unit):
    if baseUnits.isBaseUnit(unit):
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
    def isUnitless(self):
        return self._unit.isUnitless()
	
	# Magic Methods
    def __str__(self):
        return str(self._value) + ' ' + str(self._unit)
    # For now at least
    def __repr__(self):
        return self.__str__()
    
    def __mul__(self, other):
        return Measure.__rmul__(self, other)
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
    
    def __div__(self, other):
        return NotImplemented
        #return Measure.__rdiv__(self, other)
    def __rdiv__(self, other):
        if isinstance(other, Measure):
            return Measure(self._value / other._value, self._unit / other._unit)
        else:
            return NotImplemented
    
    def __add__(self, other):
        return NotImplemented
        #return Measure.__radd__(other, self)
    def __radd__(self, other):
        return NotImplemented

    def __pow__(self, other):
        return Measure(self._value ** other, self._unit ** other)
    def __rpow__(self, other):
        if self.isUnitless():
            return other ** self._value
        return NotImplemented

# A unit composed of multiple units, each with varying powers
class Unit(object):
    def __init__(self,*args):
        self._units = dict()
        for inUnit in args:
            if baseUnits.isBaseUnit(inUnit):
                inType = inUnit.getType()
                if inType not in self._units:
                    self._units[inUnit.getType()] = (inUnit, Fraction(1))
                elif self._units[inType][0] is inUnit:
                    newPower = self._units[inType][1] + power
                    if newPower != 0:
                        self._units[type] = (inUnit, newPower)
                    else:
                        self._units.pop(inType)
            elif isinstance(inUnit, Unit):
                for type, (unit, power) in inUnit._units.iteritems():
                    if type not in self._units:
                        self._units[type] = (unit, power)
                    elif self._units[type][0] is unit:
                        newPower = self._units[type][1] + power
                        if newPower != 0:
                            self._units[type] = (unit, newPower)
                        else:
                            self._units.pop(type)
                    else:
                        # TODO: Deal with converting units
                        pass
            elif len(inUnit) == 2:
                type = inUnit[0].getType()
                if type in self._units:
                    # Will need to convert to the other type
					# But really... people shouldn't be providing
					# units like "kg*slug*meter*foot", that's just silly
					pass
                else:
                    self._units[type] = (inUnit[0], Fraction(inUnit[1]))
            else:
                raise ValueError
    
    def isUnitless(self):
        return len(self._units) == 0
    
    def __str__(self):
        string = ""
        for unit, power in self._units.itervalues():
            string += unit.getAbbr() + '^(' + str(power) + ')'
        return string
    # For now repr is str
    def __repr__(self):
        return Unit.__str__(self)
    
    def __mul__(self, other):
        return Unit.__rmul__(self, other)
    def __rmul__(self, other):
        if isinstance(other, Number):
            return Measure(other, self)
        elif isinstance(other, (Unit, baseUnits.BaseUnit)):
            return Unit(self, other)
        return NotImplemented
    
    def __div__(self, other):
        #return NotImplemented
        return Unit.__rdiv__(other, self)
    def __rdiv__(self, other):
        inverseUnit = Unit(self)        # Make a copy of self
        for type, (unit, power) in self._units.iteritems():
            inverseUnit._units[type] = (unit, -1*power)
        return Unit.__rmul__(inverseUnit, other)
    
    def __pow__(self, other):
        if other == 0:
            return {}
        powerUnit = Unit(self)
        for type, (unit, power) in self._units.iteritems():
            powerUnit._units[type] = (unit, other * power)
        return powerUnit
    # rpow will probably remain not implemented as you can't really do
    # something like 4^meter
    def __rpow__(self, other):
        return NotImplemented

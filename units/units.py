# Numbers with units, makes doing math easy!
# or something like that...

from fractions import Fraction
from numbers import Number

import baseUnits

##### Objects #####
# A combination of a unit and a value
class Measure(object):
    def __init__(self, value, *args):
        self._value = value
        self._unit = Unit(*args)
	
	# Value and Unit extraction methods
    def toUnit(self, inUnit = None):
        return Measure(self._unit.convertTo(inUnit, self._value), inUnit)
    def getValue(self, desiredUnit = None):
        if desiredUnit is None:
            return self._value
        if not self.isCompatible(desiredUnit):
            raise ValueError('Incompatible units')
        return self.toUnit(desiredUnit).getValue()
    def getUnit(self):
        return self._unit
    def isUnitless(self):
        return self._unit.isUnitless()
    
	# Magic Methods
    def __str__(self):
        return str(self._value) + ' ' + str(self._unit)
    # For now repr is str
    def __repr__(self):
        return self.__str__()
    
    def __mul__(self, other):
        return Measure.__rmul__(self, other)
    def __rmul__(self, other):
        if isinstance(other, Number):
            return Measure(self._value * Number, self._unit)
        elif isinstance(other, Measure):
            otherValue = other.getValue()
            (otherValue, otherUnit) = \
                    other.getUnit().matchUnit(self.getUnit(), otherValue)
            return Measure(self._value * otherValue, self._unit * otherUnit)
        elif isinstance(other, baseUnits.BaseUnit) or isinstance(other, Unit):
            return Measure(self._value, self._unit * other)
        else:
            return NotImplemented
    
    def __div__(self, other):
        if isinstance(other, Measure):
            return Measure.__rdiv__(other, self)
        if isinstance(other, (Unit, baseUnits.BaseUnit)):
            return Measure(self._value, self._unit / other)
        return NotImplemented
    def __rdiv__(self, other):
        if isinstance(other, Measure):
            return Measure(other._value / self._value, other._unit / self._unit)
        if isinstance(other, (Unit, baseUnits.BaseUnit)):
            return Measure(1 / self._value, other / self._unit)
        else:
            return NotImplemented
    
    def __add__(self, other):
        if not isinstance(other, Measure):
            return NotImplemented
        if not self._unit.isCompatible(other._unit):
            raise ValueError('Incompatible units for addition')
        if self._unit != other._unit:
            other = other.toUnit(self._unit)
        return Measure(self._value + other._value, self._unit)
    def __radd__(self, other):
        if isinstance(other, Measure):
            return Measure.__add__(other, self)
        return NotImplemented
    
    def __sub__(self, other):
        if not isinstance(other, Measure):
            return NotImplemented
        if not self._unit.isCompatible(other._unit):
            raise ValueError('Incompatible units for subtraction')
    def __rsub__(self, other):
        if isinstance(other, Measure):
            return Measure.__sub__(other, self)
        return NotImplemented
    
    def __pow__(self, other):
        return Measure(self._value ** other, self._unit ** other)
    def __rpow__(self, other):
        if self.isUnitless():
            return other ** self._value
        raise ValueError('Exponent must be unitless')

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
                else:
                    raise ValueError("Can't combine the given units")
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
                        raise ValueError("Can't combine the given units")
            elif len(inUnit) == 2:
                type = inUnit[0].getType()
                if type not in self._units:
                    self._units[type] = (inUnit[0], Fraction(inUnit[1]))
                elif self._units[type][0] is inUnit[0]:
                    newPower = self._units[type][1] + inUnit[1]
                    if newPower != 0:
                        self._units[type] = (inUnit[0], newPower)
                    else:
                        self._units.pop(type)
                else:
                    raise ValueError("Can't combine the given units")
            else:
                raise ValueError
    
    def isUnitless(self):
        return len(self._units) == 0
    
    # Verify that the provided unit is of the same type as self
    def isCompatible(self, other):
        if len(self._units) != len(other._units):
            return False
        for key, (type, power) in self._units.iteritems():
            if key not in other._units:
                return False
            if power != other._units[key][1]:
                return False
        return True
    
    def getType(self):
        outType = {}
        for type, (unit, power) in self._units:
            outType[type] = power
        return outType
    
    def getInverse(self):
        inverseUnit = Unit(self)        # Make a copy of self
        for type, (unit, power) in self._units.iteritems():
            inverseUnit._units[type] = (unit, -1*power)
        return inverseUnit
    
    def convertTo(self, inUnit, value):
        if not self.isCompatible(inUnit):
            raise ValueError
        for type, (unit, power) in self._units.iteritems():
            if unit is not inUnit._units[type][0]:
                if not unit._isMetricBaseUnit():
                    value = unit._toMBU(value, power)
                value = inUnit._units[type][0]._fromMBU(value, power)
        return value
    
    def matchUnit(self, targetUnit, value):
        newUnit = Unit(self)
        for type, (unit, power) in self._units.iteritems():
            if type in targetUnit._units:
                if targetUnit._units[type] != (unit, power):
                    if targetUnit._units[type][1] != power:
                        raise ValueError('Power mismatch')
                    if not unit._isMetricBaseUnit():
                        value = unit._toMBU(value, power)
                        newUnit._units[type] = (unit, power)
                    value = targetUnit._units[type][0]._fromMBU(value, power)
                    newUnit._units[type] = (targetUnit._units[type][0], power)
        return (value, newUnit)
    
    def __str__(self):
        string = ""
        for unit, power in self._units.itervalues():
            string += unit.getAbbr() + '^(' + str(power) + ')'
        return string
    # For now repr is str
    def __repr__(self):
        return Unit.__str__(self)
    
    def __eq__(self, other):
        for type, unit in self._units.iteritems():
            if other._units[type] != unit:
                print other._units[type], type
                return False
        return True
    
    def __mul__(self, other):
        return Unit.__rmul__(self, other)
    def __rmul__(self, other):
        if isinstance(other, Number):
            return Measure(other, self)
        elif isinstance(other, (Unit, baseUnits.BaseUnit)):
            return Unit(self, other)
        return NotImplemented
    
    def __div__(self, other):
        if isinstance(other, Unit):
            return Unit.__rdiv__(other, self)
        if isinstance(other, baseUnits.BaseUnit):
            return Unit.__mul__(self, Unit(other).getInverse())
        return NotImplemented
    def __rdiv__(self, other):
        if isinstance(other, (Unit, baseUnits.BaseUnit)):
            return Unit.__rmul__(self.getInverse(), other)
        return NotImplemented
    
    def __pow__(self, other):
        powerUnit = Unit(self)
        if other == 0:
            powerUnit._units = {}
            return powerUnit
        for type, (unit, power) in self._units.iteritems():
            powerUnit._units[type] = (unit, other * power)
        return powerUnit
    # rpow will probably remain not implemented as you can't really do
    # something like 4^meter
    def __rpow__(self, other):
        return NotImplemented

# Special object used instead of a unit when the measure in
# question is unitless
class Unitless(object):
    pass

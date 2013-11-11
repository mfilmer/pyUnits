# Numbers with units, makes doing math easy!
# or something like that...

from numbers import Number

# Old singleton implementation. I don't like it as much as the new one
class Singelton(type):
    __instance = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instance:
            cls.__instance[cls] = super(Singelton, cls).__call__(*args, **kwargs)
        return cls.__instance[cls]

#class Singelton(type):
#    __instance = None
#    def __class__(cls, *args, **kwargs):
#        if cls is None:
#            cls.__instance = super(Singleton, cls).__call__(*args, **kwargs)
#        return cls.__instance

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

# A simple unit that is used to construct a more complicated Unit
class BaseUnit(object):
    __metaclass__ = Singelton
    _metricBaseUnit = None
    
    # metricBaseUnit is how I plan on dealing with complicated conversions
    # everything will be required to have a conversion to and from
    # the "metricBaseUnit"
    def _getMetricBaseUnit(self):
        return self._metricBaseUnit
    
    def _isMetricBaseUnit(self):
        self.getMetricBaseUnit() is self
    
    # Methods to convert either to or from another unit
    # These should be implemented for all units other than the metricBaseUnit
    def _convertTo(self, other):
        return NotImplemented
    def _convertFrom(self, other):
        return NotImplemented
    
    # Deal with multiplication
    # Individual units should override _mul and _rmul
    def __mul__(self, other):
        return NotImplemented
    def __rmul__(self, other):
        return NotImplemented
# Maybe how I will deal with more complicated units such as Joules (kg*m^2/s^2)
class CompositeUnit(object):
    __metaclass__ = Singelton

# Units that are from the metric system will inherit from this class
# It will do something in the future to make conversions easier
class Metric(object):
    pass

# Unitless is a special case unit type
class Unitless(BaseUnit):
    pass

# Units grouped by type
class Distance(BaseUnit):
    pass
class Meter(Distance, Metric):
    def __init__(self):
        Distance._metricBaseUnit = self
meter = Meter()
class Foot(Distance):
    pass
foot = Foot()

class Mass(BaseUnit):
    pass
class Kilogram(Mass, Metric):
    def __init__(self):
        Mass._metricBaseUnit = self
kilogram = Kilogram()
class Slug(Mass):
    pass
slug = Slug()

class Time(BaseUnit):
    pass
class Second(Time, Metric):
    def __init__(self):
        Time._metricBaseUnit = self
second = Second()

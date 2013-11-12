from numbers import Number

import units

class Singelton(type):
    __instance = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instance:
            cls.__instance[cls] = super(Singelton, cls).__call__(*args, **kwargs)
        return cls.__instance[cls]

# A simple unit that is used to construct a more complicated Unit
class BaseUnit(object):
    __metaclass__ = Singelton
    _metricBaseUnit = None
    _type = None
    
    # metricBaseUnit is how I deal with complicated conversions
    # every unit is required to have a conversion to and from
    # the "metricBaseUnit"
    def _getMetricBaseUnit(self):
        return self._metricBaseUnit
    def _isMetricBaseUnit(self):
        self.getMetricBaseUnit() is self
    def getType(self):
        return self._type
    
    # Methods to convert either to or from another unit
    # These should be implemented for all units other than the metricBaseUnit
    def _convertTo(self, other):
        return NotImplemented
    def _convertFrom(self, other):
        return NotImplemented
    
    # Text representation of a unit
    def getAbbr(self):
        return self._abbr
    def getName(self):
        return self._name
    def getNames(self):
        return self._names
    def __str__(self):
        return self._name
    
    # Deal with multiplication
    # Individual units should override _mul and _rmul
    def __mul__(self, other):
        return NotImplemented
    def __rmul__(self, other):
        if isinstance(other, Number):
            return units.Measure(other, self)

# Units that are from the metric system will inherit from this class
# It will do something in the future to make conversions easier
class Metric(object):
    pass

##### Units #####
# Unitless is a special case unit type
class Unitless(BaseUnit):
    pass

# Units grouped by type
class Distance(BaseUnit):
    def __new__(cls):
        Distance._type = Distance
        return super(Distance, cls).__new__(cls)
class Meter(Distance, Metric):
    _name = 'meter'
    _names = 'meters'
    _abbr = 'm'
    def __init__(self):
        Distance._metricBaseUnit = self
meter = Meter()
class Foot(Distance):
    _name = 'foot'
    _names = 'feet'
    _abbr = 'ft'
foot = Foot()

class Mass(BaseUnit):
    def __new__(cls):
        Mass._type = Mass
        return super(Mass, cls).__new__(cls)
class Kilogram(Mass, Metric):
    _name = 'kilogram'
    _names = 'kilograms'
    _abbr = 'kg'
    def __init__(self):
        Mass._metricBaseUnit = self
kilogram = Kilogram()
class Slug(Mass):
    _name = 'slug'
    _names = 'slugs'
    _abbr = 'slugs'
slug = Slug()

class Time(BaseUnit):
    def __new__(cls):
        Time._type = Time
        return super(Time, cls).__new__(cls)
class Second(Time, Metric):
    _name = 'second'
    _names = 'seconds'
    _abbr = 's'
    def __init__(self):
        Time._metricBaseUnit = self
second = Second()
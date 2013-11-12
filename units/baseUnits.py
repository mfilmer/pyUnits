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
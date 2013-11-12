import math
from fractions import Fraction

import units

def sqrt(inMeasure):
    return units.Measure(math.sqrt(inMeasure.getValue()), 
    inMeasure.getUnit()**Fraction(1,2))
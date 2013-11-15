pyUnits
=======

pyUnits is a python module designed to make calculations involving units easy.
pyUnits has an object oriented background, but is designed such that the user
rarely if ever needs to create an object or call a method. 

pyUnits has a variety of built in units, and is easily expandable to support
any units that are required. Units included so far:
- meter
- foot
- kilogram
- slug
- second

pyUnits stores these internally as a singleton. These objects are accessible
as in the following example:
```python
>>> import units
>>> units.meter
<units.baseUnits.Meter object at 0x0000000001F1A160>
```

Measure Object
--------------

The Measure object is how the combination of a numerical value and a unit is
stored. Measure objects are automatically created when a unit is multiplied by
a number as in the following example:
```python
>>> a = 5 * units.meter
>>> type(a)
<class 'units.units.Measure'>
```

Calling `str()` on a Measure object returns a human readable representation of
the value stored:
```python
>>> str(5 * units.meter)
5 m^(1)
```

### More complicated units

Individual units can be combined into more complicated units by multiplying
the simple units together:
```python
>>> 5 * (units.meter * units.second)
5 m^(1)s^(1)
```
Alternatively, you can multiply a unit by a Measure:
```python
>>> (5 * units.meter) * units.second
5 m^(1)s^(1)
```
and finally, you can multiply two Measures together:
```python
>>> (5 * units.meter) * (2 * units.second)
10 m^(1)s^1
```

### Other operations

pyUnits also supports addition, subtraction, division, and exponentiation:
```python
>>> 5 * units.meter + 2*units.meter
7 m^(1)
>>> 2 * units.meter - 5 * units.meter
-3 m^(1)
>>> 10 * units.meter / (2 * units.second)
5 m^(1)s^(-1)
>>> (2 * units.meter)**2
4 m^(2)
```

## Unit Conversions

In some cases, the measures you wish to add or multiply together are of
different units. In that case, one set of units is converted into the other
before the operation occurs:
```python
>>> 1 * units.meter + 2 * units.foot
1.60957025297 m^(1)
>>> (2 * units.meter) * (3 * units.foot)
1.60957025297 m^(1)
```

Care should be taken to not try to multiply units (not measures) that are of
the same type but different units together:
```python
>>> units.meter * units.foot
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "units\baseUnits.py", line 59, in __mul__
    return BaseUnit.__rmul__(self, other)
  File "units\baseUnits.py", line 64, in __rmul__
    return units.Unit(self, other)
  File "units\units.py", line 113, in __init__
    raise ValueError("Can't combine the given units")
ValueError: Can't combine the given units
```

### Getting the units you want

Once you have completed your calculations and you are ready for the final
result, you can convert your measure into any units you want that are
compatible with it's type:
```python
>>> a = 5 * units.meter * units.second
>>> a.toUnit(units.foot * units.second)
16.405 ft^(1)s^(1)
```
This just returns a new Measure, it does not modify the existing measure:
```python
>>> a
5 m^(1)s^(1)
```
Once the measure is in the desired units, you can extract the value and
units individually:
```python
>>> a = 5 * units.meter * units.second
>>> a = a.toUnit(units.foot * units.second)
>>> a.getValue()
16.405
>>> a.getUnit()
ft^(1)s^(1)
```
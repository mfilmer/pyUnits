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

The Measure() object is how the combination of a numerical value and a unit is
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
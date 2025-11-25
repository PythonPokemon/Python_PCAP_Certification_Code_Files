"""
Selected functions from the math module:

The first group of the 's functions are connected with trigonometry:math

sin(x) → the sine of x;
cos(x) → the cosine of x;
tan(x) → the tangent of x.
"""

from math import pi, radians, degrees, sin, cos, tan, asin

ad = 90
ar = radians(ad)
ad = degrees(ar)

print(ad == 90.)
print(ar == pi / 2.)
print(sin(ar) / cos(ar) == tan(ar))
print(asin(sin(ar)) == ar)

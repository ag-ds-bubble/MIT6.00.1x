# Imports
from math import tan, pi

def polysum(n,s):
    # Polygon Area
    area = (n*(s**2))/4
    area /= tan(pi/n)
    # Polygon Perimeter
    perimeter = n*s
    # Required Sum and Rounding up
    _sum = round(area+perimeter**2,4)
    return _sum
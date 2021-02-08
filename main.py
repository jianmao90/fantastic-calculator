import areaCalc 
import perimCalc 
import numpy as np
import volume

# Square demo
a=5
area=areaCalc.square(a)
perimeter=perimCalc.square(a)
print('For a square of length %d, the area is %d and the perimeter %d'
%(a,area,perimeter))
# Cube demo
a=5
vol=volume.cube(a)
print('The volume of a cube of size %d is %d'%(a,vol))

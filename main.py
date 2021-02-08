import areaCalc 
import perimCalc 
import numpy as np

# Square demo
a=5
area=areaCalc.square(a)
perimeter=perimCalc.square(a)
print('For a square of length %d, the area is %d and the perimeter %d'
%(a,area,perimeter))

r=2
area_circle = areaCalc.circle(r)
perimeter_circle = perimCalc.circle(r)
print('For a circle of radius %d, the area is %d and the circumference is %d'%(r, area_circle, perimeter_circle))

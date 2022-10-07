import cmath
import math
z=complex(5,5)
print('z=',z.real,z.imag)
fi=math.atan(z.imag/z.real)
print('abs_math=', math.sqrt(z.imag*z.imag+z.real*z.real))
print('phase=',math.degrees(fi))

print( math.degrees(cmath.phase(z)))
print( (cmath.polar(z)))

val = cmath.polar(5 + 5j)
print(val[0])
print(math.degrees(val[1]))





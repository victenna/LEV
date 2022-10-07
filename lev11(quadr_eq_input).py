

import math  # Makes the math library available.
a = float(input("Enter coefficient A: "))
b = float(input("Enter coefficient B: "))
c = float(input("Enter coefficient C: "))
q=b * b - 4 * a * c
if q>=0:
    discRoot = math.sqrt(b * b - 4 * a * c)
    root1 = (-b + discRoot) / (2 * a)
    root2 = (-b - discRoot) / (2 * a)
    print("The solutions are:", root1, root2 )
else:
    print('No solution')
        


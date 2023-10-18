#number 1
import math
degree = 15
radian = math.radians(degree)
print("Degree: ", degree)
print("Radian: ", radian)

#number 2
base = 5
height = 6
area = base * height
print("Length of base: ", base)
print("Height of parallelogram: ", height)
print("Area is: ", area)

#number 3
def smallest_multiple(n):
    if n <= 2:
        return n
    i = n * 2
    factors = [number for number in range(n, 1, -1) if number * 2 > n]
    print(factors)
    while True:
        for a in factors:
            if i % a != 0:
                i += n
                break
        if a == factors[-1] and i % a == 0:
            return i

#number4
n = 13
print("If n =", n)
print("Expected Output:")
print("[13, 12, 11, 10, 9, 8, 7]")
print(smallest_multiple(n))

#number 5
import numpy as np

a = np.array([1+1j, 1+0j, 4.5, 3, 2, 2j])
print("Original array")
print(a)

print("Checking for complex number:")
print(np.iscomplex(a))

print("Checking for real number:")
print(np.isreal(a))

print("Checking for scalar type:")
print(np.isscalar(3.1))
print(np.isscalar([3.1]))


import numpy as np

X = np.array([1,7,13,105])
print("Original array:")
print(X)

memory_size = X.size * X.itemsize

print("Size of the memory occupied by the said array:")
print(memory_size,"bytes")
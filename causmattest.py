import numpy as np
import causet as cs

#testing that the causalmatrix is correctly calculated by causDiam
#this is not the most efficient way to calculate the entries of c and tests if 
#the vectorization in its implementation in causDiam is done correctly

d = 4
c, t, x = cs.causDiam(1000, d)

ds2 = 0.
finalTruth = True

for i in range(1000):
    for j in range(1000):
        ds2 = -(t[0, j] - t[0, i])**2
        ds2 = ds2 + (x[0, j] - x[0, i])**2
        if (d == 3) or (d == 4):
            ds2 = ds2 + (x[1, j] - x[1, i])**2
        if d == 4:
            ds2 = ds2 + (x[2, j] - x[2, i])**2
        tempBool = (ds2 < 0) and (t[0, i] < t[0, j])
        finalTruth = (finalTruth and (tempBool == c[i, j]))

#finalTruth should be True at the end of these loops

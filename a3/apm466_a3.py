"""apm466_a3_JinxuanZhang.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10ESbiPoFqwpDvq4EsgaBCsklBd90ww4l

# APM466 Assignment 3: Credit Risk
"""

import math
import numpy as np
from scipy import linalg

"""## Question 1

### Part (a)
"""

P = np.matrix([[7/10, 2/10, 1/10, 0],
              [1/10, 5/10, 2/10, 2/10],
              [1/10, 3/10, 3/10, 3/10],
              [0, 0, 0, 1]])

np.linalg.matrix_power(P, 3)

"""### Part (b)"""

##### implementation of function for finding the matrix fractional powers #####
# this returns similar results as scipy.linalg.fractional_matrix_power

def frac_comb(n, r):
    '''
    Calculates combinations function (nCr) with fractional numbers,
    noting that scipy.special.comb only works for integers
    '''
    k = 0
    prod = 1
    while k < r:
        prod *= (n-k)
        k +=1

    return prod/math.factorial(r)


def frac_pow(M, p, ep):
    '''
    Finds fractional power of a matrix with iterative approach until convergence
        M - input matrix
        p - fractional power
        ep - convergence threshold
    '''
    k = 0
    sum = np.zeros((4,4))
    prev = np.matrix.copy(sum)
    diff = 999
    
    while diff > ep:
        sum += frac_comb(p, k) * np.linalg.matrix_power(M-np.identity(4), k)
        diff = np.linalg.norm(sum-prev)
        prev = np.matrix.copy(sum)
        k += 1

    return sum

linalg.fractional_matrix_power(P, 1/6)

"""### Part (c)"""

np.linalg.matrix_power(P, 10000)

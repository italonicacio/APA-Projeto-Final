
from typing import Any
import numpy as np
from math import sqrt
from math import floor

def euc(v1,v2):
    return floor(sqrt((v1[0] - v2[0])**2 + (v1[1] - v2[1])**2))

def ReadInstance(filePath):

    file = open(filePath, 'r')

    aux = file.readline().split()
    n = int(aux[1])

    aux_matrix = np.zeros((n,n))

    aux = file.readline().split()
    p = int(aux[1])

    next(file)    

    for line, i in zip(file, range(n)):
        aux_matrix[i] = list(map(float, line.split()))

    print('Dim: {}'.format(n))
    print('p: {}'.format(p))
    print('Cost Matrix:')
    print(aux_matrix)

    file.close()

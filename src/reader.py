
from problem import Problem

import numpy as np
   

def ReadInstance(file_name):

    file = open(file_name, 'r')

    aux = file.readline().split()
    n = int(aux[1])

    cost_matrix = np.zeros((n,n))

    aux = file.readline().split()
    p = int(aux[1])

    next(file)    

    for line, i in zip(file, range(n)):
        cost_matrix[i] = list(map(float, line.split()))
    
    file.close()

    return Problem(n, p, cost_matrix)

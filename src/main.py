from numpy.lib.function_base import copy
from reader import *



def main():

    # file_name = 'instances/n10p4.txt'
    # file_name = 'instances/n52p11.txt'
    file_name = 'instances_apa_cup/cup3.txt'

    problem = ReadInstance(file_name)
    
    
    problem.NearestNeighbor()
  
    for route in problem.routes:
        problem.TwoOPT(route)
    problem.SaveSolution()
   
    


if __name__ == "__main__":
    main()
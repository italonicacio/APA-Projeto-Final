from numpy.core.numeric import Inf
from pandas.core import algorithms
from reader import *
import time
import pandas as pd
from pandas.plotting import table
import matplotlib.pyplot as plt

def TimeMeasurement(function, *args, **kwargs):
    start_time = time.time()
    function(*args, **kwargs)
    end_time = time.time()

    return round((end_time - start_time) * 1000)#milliseconds
        

def CreateRowForTable(problem, function, *args, **kwargs):
    mean_time = 0.0
    mean_cost = 0.0
    best_cost = Inf
    max_interation = 10
    for i in range(0, max_interation):

        time = TimeMeasurement(function,*args, **kwargs)
        cost = problem.TotalCost()
        if cost < best_cost:
            best_cost = cost
            
        mean_cost = mean_cost + cost
        mean_time = mean_time + time

    mean_time = mean_time/max_interation
    mean_cost = mean_cost/max_interation
    return mean_time, mean_cost, best_cost

def main():

    
    instances = [  'instances/n10p4.txt',
                   'instances/n15p5.txt',
                   'instances/n29p7A.txt',
                   'instances/n29p8B.txt',
                   'instances/n40p11.txt',
                   'instances/n52p11.txt',
                   'instances_apa_cup/cup1.txt',
                   'instances_apa_cup/cup2.txt',
                   'instances_apa_cup/cup3.txt']
   
    
    columns_label = ['Media da solução', 'Melhor Solução', 'Media do tempo']
    algorithms = ['Heuristica Construtiva', 'VND']
    columns = pd.MultiIndex.from_product([algorithms, columns_label])
    df = pd.DataFrame(columns=columns, index=instances)
    print(df)
    
    for instance in instances:
        problem = ReadInstance(instance)
        
        print('Instance:', instance[10:])
        row = []
        mean_time, mean_cost, best_cost = CreateRowForTable(problem, problem.NearestNeighbor)
        row.append([mean_time, best_cost, mean_cost])
        print('Nearest Neigh')
        print(f"Time {mean_time}")
        print(f"Cost {mean_cost}")
        print(f"Best Cost {best_cost}\n")

        
        mean_time, mean_cost, best_cost = CreateRowForTable(problem, problem.VND, problem.routes)
        print('VND')
        print(f"Time {mean_time}")
        print(f"Cost {mean_cost}")
        print(f"Best Cost {best_cost}\n")
        
        row.append([mean_time, best_cost, mean_cost])
        print(row)
        
   
    
    
    
if __name__ == "__main__":
    main()





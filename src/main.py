from numpy.core.numeric import Inf
from reader import *
import time
import pandas as pd


def TimeMeasurement(function, *args, **kwargs):
    start_time = time.time()
    function(*args, **kwargs)
    end_time = time.time()

    return round((end_time - start_time) * 1000, 4)  #milliseconds
        

def CreateDataForTable(problem, function, *args, **kwargs):
    mean_time = 0.0
    mean_cost = 0.0
    best_cost = Inf
    max_interation = 5
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
                   'instances/n52p11.txt']
   
    
    data = []
    
    for instance in instances:
        problem = ReadInstance(instance)
        
        row = []
        mean_time, mean_cost, best_cost = CreateDataForTable(problem, problem.NearestNeighbor)
        row.append(mean_cost)
        row.append(best_cost)
        row.append(mean_time)
        
        mean_time, mean_cost, best_cost = CreateDataForTable(problem, problem.VND, problem.routes)
        
        row.append(mean_cost)
        row.append(best_cost)
        row.append(mean_time)
        
        data.append(row)

        
        
    
    columns_label = ['Media da solução', 'Melhor Solução', 'tempo(ms)']
    algorithms = ['Heuristica Construtiva', 'VND']
    columns = pd.MultiIndex.from_product([algorithms, columns_label])
    df = pd.DataFrame(data, columns=columns, index=instances)
    print(df)


def mainCup():
    
    instances = [  'instances/n10p4.txt',
                   'instances/n15p5.txt',
                   'instances/n29p7A.txt',
                   'instances/n29p8B.txt',
                   'instances/n40p11.txt',
                   'instances/n52p11.txt']

    instances_cup = [   'instances_apa_cup/cup1.txt',
                        'instances_apa_cup/cup2.txt',
                        'instances_apa_cup/cup3.txt']
   
    for instance in instances_cup:
        problem = ReadInstance(instance)

        print(problem.file_name[18:])

        print('Heuristica de Teste com vizinho mais proximo e o 2opt melhorado')
        mean_time, mean_cost, best_cost = CreateDataForTable(problem, problem.HeuristicTest)
        print('Custo Medio: ',mean_cost)
        print('Melhor Custo:',best_cost)
        print('tempo medio:',mean_time)
        

        print('VND')
        mean_time, mean_cost, best_cost = CreateDataForTable(problem, problem.VND, problem.routes)
        print('Custo Medio: ',mean_cost)
        print('Melhor Custo:',best_cost)
        print('tempo medio:',mean_time)
        
        print()

        problem.SaveSolution(problem.file_name[18:])

    
if __name__ == "__main__":
    main()

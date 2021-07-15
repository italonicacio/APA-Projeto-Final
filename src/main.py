from numpy.core.fromnumeric import mean
from numpy.core.numeric import Inf
from reader import *
import time

def TimeMeasurement(function, *args, **kwargs):
    start_time = time.time()
    function(*args, **kwargs)
    end_time = time.time()

    return (end_time - start_time) * 1000#milliseconds
        

def CreateRowForTable(problem, function, *args, **kwargs):
    mean_time = 0.0
    mean_cost = 0.0
    best_cost = Inf
    max_interation = 1000
    for i in range(0, max_interation):

        time = TimeMeasurement(function,*args, **kwargs)
        cost = problem.TotalCost()
        if cost < best_cost:
            best_cost = cost
            
            if 'instances_apa_cup/cup1.txt' == problem.file_name:
                problem.SaveSolution('cup1.out')
            elif 'instances_apa_cup/cup2.txt' == problem.file_name:
                problem.SaveSolution('cup2.out')
            elif 'instances_apa_cup/cup3.txt' == problem.file_name:
                problem.SaveSolution('cup3.out')
            
        mean_cost = mean_cost + cost
        mean_time = mean_time + time

    mean_time = mean_time/max_interation
    mean_cost = mean_cost/max_interation
    return mean_time, mean_cost, best_cost

def main():

    
    instances = [ 'instances/n10p4.txt',
                   'instances/n15p5.txt',
                   'instances/n29p7A.txt',
                   'instances/n29p8B.txt',
                   'instances/n40p11.txt',
                   'instances/n52p11.txt',
                   'instances_apa_cup/cup1.txt',
                   'instances_apa_cup/cup2.txt',
                   'instances_apa_cup/cup3.txt']
   
    
    for instance in instances:
        problem = ReadInstance(instance)
        
        print('Instance:', instance[10:])
        mean_time = 0
        mean_cost = 0
        best_cost = 0
        mean_time, mean_cost, best_cost = CreateRowForTable(problem, problem.NearestNeighbor)
        print('Nearest Neigh')
        print(f"Time {mean_time}")
        print(f"Cost {mean_cost}")
        print(f"Best Cost {best_cost}\n")

        mean_time = 0
        mean_cost = 0
        best_cost = 0
        mean_time, mean_cost, best_cost = CreateRowForTable(problem, problem.VND, problem.routes)
        print('VND')
        print(f"Time {mean_time}")
        print(f"Cost {mean_cost}")
        print(f"Best Cost {best_cost}\n")

        
            


    
    
    
    
if __name__ == "__main__":
    main()





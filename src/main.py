from copy import deepcopy
from reader import *


def main():

    # file_name = 'instances/n10p4.txt'
    # file_name = 'instances/n52p11.txt'
    # file_name = 'instances_apa_cup/cup1.txt'
    # file_name = 'instances_apa_cup/cup2.txt'
    file_name = 'instances_apa_cup/cup3.txt'


    problem = ReadInstance(file_name)
    
    
    problem.NearestNeighbor()
    # print(problem.routes[0])
    
    test_routes = deepcopy(problem.routes)
    best_cost = problem.RouteCost(test_routes[0])
    best_route = test_routes[0]

    

    for route in problem.routes:
        problem.TwoOPT(route)

    for route in test_routes:
        best_cost = problem.RouteCost(route)
        best_route = route
        improve  = 0

        while improve < 20:
            new_route, new_cost = problem.TestTwoOPT(best_route)

            if new_cost < best_cost:
                improve = 0
                best_cost = new_cost
                best_route = new_route
            else: 
                improve += 1
            
        route[:] = best_route

    print(problem.TotalCost())

    print(problem.TotalCost(test_routes))

    print(problem.routes == test_routes)


    # for route in problem.routes:
    #     problem.TwoOPT(route)

    # for route in test_routes:
    #     problem.TestTwoOPT(route)

    # print(problem.routes) 
    # print(problem.TotalCost())

    # print(test_routes) 
    # print(problem.TotalCost(test_routes))

    # # file_name_save = 'cup2.txt'
    # problem.SaveSolution()
 
    
if __name__ == "__main__":
    main()
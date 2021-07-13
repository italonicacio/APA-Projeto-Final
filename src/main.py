from reader import *

def main():

    file_name = 'instances/n10p4.txt'
    # file_name = 'instances/n52p11.txt'
    # file_name = 'instances_apa_cup/cup1.txt'
    # file_name = 'instances_apa_cup/cup2.txt'
    # file_name = 'instances_apa_cup/cup3.txt'


    problem = ReadInstance(file_name)
    
    
    problem.NearestNeighbor()
    test_routes = problem.routes.copy()

    for route in problem.routes:
        problem.TwoOPT(route)

    for route in test_routes:
        problem.TestTwoOPT(route)

    print(problem.routes) 
    print(problem.TotalCost())

    print(test_routes) 
    print(problem.TotalCost(test_routes))

    # file_name_save = 'cup3.txt'
    # problem.SaveSolution()
 

if __name__ == "__main__":
    main()
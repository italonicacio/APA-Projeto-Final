from reader import *


def main():

    file_name = 'instances/n10p4.txt'
    # file_name = 'instances/n52p11.txt'
    problem = ReadInstance(file_name)
    
    
    problem.NearestNeighbor()
    print(problem.RouteCost(problem.routes[0]))
    problem.SaveSolution()
   

    


if __name__ == "__main__":
    main()
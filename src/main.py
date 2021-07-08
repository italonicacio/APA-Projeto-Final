

from reader import *


def main():
    # file_name = 'instances/n10p4.txt'
    file_name = 'instances/n52p11.txt'
    problem = ReadInstance(file_name)
    
    solution = problem.NearestNeighbor()
    print(solution)


if __name__ == "__main__":
    main()
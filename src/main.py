

from reader import *


def main():
    file_name = 'instances/n10p4.txt'
    problem = ReadInstance(file_name)
    
    problem.NearestNeighbor()
    


if __name__ == "__main__":
    main()


from reader import *



def main():
    file_name = '../instances/n10p4.txt'
    problem = ReadInstance(file_name)
    
    print('Dim: {}'.format(problem.n))
    print('p: {}'.format(problem.p))
    print('Cost Matrix:')
    print(problem.cost_matrix)


if __name__ == "__main__":
    main()

from numpy import where, amin

class Problem:

    def __init__(self, n, p, cost_matrix):
        self.n = n
        self.p = p
        self.cost_matrix = cost_matrix

    def NearestNeighbor(self):

        solution = []
        all_vertices_visited =  False
        flags = [False for i in range(0, self.n)]
        
        total_agents = 0
        current_vertex = 0
        while(not all_vertices_visited):
            
            k = 0
            while(k < self.p):
                
                neighbor_vertex  = where( (self.cost_matrix[current_vertex] == amin(self.cost_matrix[current_vertex])) != (flags == False))[0][0]
                
                print( (self.cost_matrix[current_vertex] == amin(self.cost_matrix[current_vertex])) != (flags == False ) )
                print(current_vertex," ", neighbor_vertex)

                if flags[neighbor_vertex] == False:
                    flags[neighbor_vertex] = True
                    current_vertex = neighbor_vertex
                else:
                    all_vertices_visited = flags == True
                    break

                print(flags)
                print()

                

                k +=1
            
            total_agents += 1
            all_vertices_visited = True
                    

        return solution

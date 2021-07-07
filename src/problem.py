from numpy import where, amin, Inf



class Problem:

    def __init__(self, n, p, cost_matrix):
        self.n = n
        self.p = p
        self.cost_matrix = cost_matrix

    def NearestNeighbor(self):

        solution = []
        all_vertices_visited =  False
        visited_vertices  = [False for i in range(0, self.n)]
        visited_vertices[0] = True
        total_agents = 0
        current_vertex = 0
        iteration = 0
        solution.append(current_vertex)


        while(not all_vertices_visited):
            
            k = 0

            while(k <= self.p):
                
                if( all(visited_vertices)):
                    break

                aux = 0
                min_value = Inf
                for j in range(0, self.n):
                    
                    if current_vertex != j:
                        
                        if self.cost_matrix[current_vertex][j] < min_value and visited_vertices[j] == False:
                            min_value = self.cost_matrix[current_vertex][j]
                            aux = j

                current_vertex = aux
                solution.append(current_vertex)
                visited_vertices[current_vertex] = True
                print(visited_vertices)
                print(current_vertex) 

                k +=1

            
            current_vertex = 0
            solution.append(current_vertex)            
            
            total_agents += 1
            
            iteration += 1
            all_vertices_visited =  all(visited_vertices)

        print(visited_vertices) 

        return solution



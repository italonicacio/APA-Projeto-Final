from numpy import Inf
import numpy as np



class Problem:

    def __init__(self, n, p, cost_matrix):
        self.n = n
        self.p = p
        self.cost_matrix = cost_matrix
        self.routes = []

    def NearestNeighbor(self):

        all_vertices_visited =  False
        visited_vertices  = [False for i in range(0, self.n)]
        visited_vertices[0] = True
        total_agents = 0
        current_vertex = 0
        iteration = 0

        while(not all_vertices_visited):
            
            k = 0
            solution = []
            solution.append(current_vertex)

            while(k < self.p):
                
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

                k +=1

            
            current_vertex = 0
            solution.append(current_vertex)            
            
            self.routes.append(solution)
            total_agents += 1
            
            iteration += 1
            all_vertices_visited =  all(visited_vertices)

        

        return self.routes

    def RouteCost(self, route):
        total_cost = 0

        current_vertex = 0
            
        for neighbor_vertex in route:
                
            if neighbor_vertex != 0:
                total_cost += self.cost_matrix[current_vertex][neighbor_vertex]
                current_vertex = neighbor_vertex
        
        total_cost += self.cost_matrix[current_vertex][0]

        return total_cost


    def TotalCost(self):
        total_cost = 0

        for route in self.routes:
            total_cost += self.RouteCost(route)

        return total_cost

    def SaveSolution(self, file_name_to_save = 'solution.txt'):
        
        file = open(file_name_to_save, 'w')
        for route in self.routes:
            file.write(', '.join(map(str, route))+'; ')
        
        file.write('\nCost of Solution: '+str(self.TotalCost()))
        file.close()



    # def TwOPTSwap(route):

    

    def TwoOPT(self, route):

        best_route = route.copy()
        best_cost = self.RouteCost(best_route)



        improve = 0

        while improve < 20:

            for i in range(0, self.n-1):
                for j in range(i+1, self.n):
                    print(j)

            
            improve += 1

            print(improve)




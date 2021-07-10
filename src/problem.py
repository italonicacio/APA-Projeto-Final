from numpy import Inf
from math import floor



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



    def TwOPTSwap(self, route, i, j, size):
        new_route = []
        for c in range(0, i):
            new_route.append(route[c])

        dec = 0        
        for c in range(i, j+1):
            new_route.append(route[j - dec])
            dec += 1

        for c in range(j +1, size):
            new_route.append(route[c])
    
        return new_route

    def TwoOPT(self, route):

        best_route = route.copy()
        new_route = best_route.copy()
        best_cost = self.RouteCost(best_route)
        
        size = len(route)
        # print(best_route)
        # print(best_cost)


        improve = 0
        max_iteration = 20

        while improve < max_iteration:
            best_cost = self.RouteCost(best_route)
            
            for i in range(0, size-1):
                for j in range(i+1, size):
                    
                    # if (j-i) == 1:
                    #     aux = new_route[j]
                    #     new_route[j] = new_route[i]
                    #     new_route[i] = aux
                    # else:
                    #     for k in range(0, floor((j-i)/2)):
                            
                    #         aux = new_route[j-k]
                    #         new_route[j-k] = new_route[i+k]
                    #         new_route[i+k] = aux  
                    new_route = self.TwOPTSwap(best_route, i,j, size)
                    new_cost = self.RouteCost(new_route)

                    if(new_cost < best_cost):
                        improve = 0
                        best_route = new_route.copy()
                        best_cost = new_cost
                        # print(best_cost)
                        
            
            improve += 1

        
        # print(best_route)
        # print(best_cost)
        route[:] = best_route





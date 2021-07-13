from numpy import Inf
from typing import overload, Any


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

    # VND = Variable Neighbourhood Descent
    def VND(self):
        best_solution = self.NearestNeighbor()
        new_solution = best_solution
        k = 0
        local_search = [self.TwoOPT]
        while k < len(local_search):
            
            local_search[k](new_solution)
            if self.TotalCost(new_solution) < self.TotalCost(best_solution):
                best_solution = new_solution
                k = 1
            else:
                k += 1
                

    def RouteCost(self, route):
        total_cost = 0

        current_vertex = 0
            
        for neighbor_vertex in route:
                
            if neighbor_vertex != 0:
                total_cost += self.cost_matrix[current_vertex][neighbor_vertex]
                current_vertex = neighbor_vertex
        
        total_cost += self.cost_matrix[current_vertex][0]

        return total_cost        

    def TotalCost(self, routes = None):

        total_cost = 0
        
        if not routes:
            for route in self.routes:
                total_cost += self.RouteCost(route)
        else:
            for route in routes:
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

    def TwoOPT(self, route, max_iteration = 20):

        best_route = route.copy()
        # new_route = best_route.copy()
        best_cost = self.RouteCost(best_route)
        
        size = len(best_route)
        
        improve = 0

        while improve < max_iteration:
            best_cost = self.RouteCost(best_route)
            
            for i in range(1, size-1):
                for j in range(i+1, size):
                    new_route = self.TwOPTSwap(best_route, i,j, size)
                    new_cost = self.RouteCost(new_route)

                    if(new_cost < best_cost):
                        improve = 0
                        best_route = new_route.copy()
                        best_cost = new_cost
                                              
            
            improve += 1
        
        route[:] = best_route

    def TestTwOPTSwap(self, route, i, j, size):
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

    def TestTwoOPT(self, route, max_iteration = 20):

        best_route = route.copy()
        # new_route = best_route.copy()
        best_cost = self.RouteCost(best_route)
        
        size = len(best_route)
        
        improve = 0

        while improve < max_iteration:
            # best_cost = self.RouteCost(best_route)
            
            for i in range(1, size-1):
                for j in range(i+1, size):
                    new_route = self.TwOPTSwap(best_route, i,j, size)
                    new_cost = self.RouteCost(new_route)

                    if(new_cost < best_cost):
                        improve = 0
                        best_route = new_route.copy()
                        best_cost = new_cost
                                              
            
            improve += 1
        
        route[:] = best_route





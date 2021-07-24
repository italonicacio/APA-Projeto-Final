from numpy import Inf


class Problem:

    def __init__(self, n, p, cost_matrix, file_name = None):
        self.n = n
        self.p = p
        self.cost_matrix = cost_matrix
        self.routes = []
        self.file_name = file_name

    def HeuristicTest(self):
        self.routes = []
        all_vertices_visited =  False
        visited_vertices  = [False for i in range(0, self.n)]
        visited_vertices[0] = True
        total_agents = 0
        current_vertex = 0
        iteration = 0
        
        solution = []
        solution.append(current_vertex)  
        while(not all_vertices_visited):
            

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
           
            
            
            total_agents += 1
            
            iteration += 1
            all_vertices_visited =  all(visited_vertices)

        current_vertex = 0
        solution.append(current_vertex)  

        # self.ModifiedTwoOPT(solution)
        
        self.VND([solution])
        
        k = 0
        route = []
        for i in range(0, len(solution) - 1):

            
            route.append(solution[i])
            if solution[i] != 0:
                k += 1

            if k == self.p:
                k = 0
                route.append(0)
                self.routes.append(route)
                route = []
                route.append(0)

        route.append(0)
        self.routes.append(route)

    def NearestNeighbor(self):
        self.routes = []
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
    def VND(self, routes):
        
        local_search = [self.ModifiedTwoOPT, self.Swap, self.TwoOPT]
        for i in range(0, len(routes)):
            
            best_route = routes[i]
            new_route = best_route
            k = 0
            while k < len(local_search):
                local_search[k](new_route)
                if self.RouteCost(new_route) < self.RouteCost(best_route):
                    best_route = new_route
                    k = 0
                else:
                    k += 1
                
            routes[i] = best_route

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

    def TwOPTSwap(self, route, i, j):

        size = len(route)
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

    def TwOPTSwapSimulation(self, route, i, j, cost):
        
        aux_cost = cost
        for c in range(i, j+2):
            aux_cost -= self.cost_matrix[route[c-1]][route[c]]

        dec = 0
        current = i -1
        for c in range(i, j+1): 
            aux_cost += self.cost_matrix[route[current]][route[j - dec]]
            current = j - dec
            dec += 1
        
        aux_cost += self.cost_matrix[route[current]][route[j+1]]
        return aux_cost

    def TwoOPT(self, route):

        best_route = route.copy()
        
        best_cost = self.RouteCost(best_route)
        best_i = 0
        best_j = 0
        
        size = len(best_route)
         
        for i in range(1, size-1):
            for j in range(i+1, size - 1):
                new_cost = self.TwOPTSwapSimulation(best_route, i , j, best_cost)
                    
                if(new_cost < best_cost):
                        
                    best_i = i
                    best_j = j
                    best_cost = new_cost
                                              
        
        best_route = self.TwOPTSwap(best_route, best_i, best_j)

        route[:] = best_route

    def ModifiedTwoOPT(self, route, max_iteration = 10):

        best_route = route
        best_cost = self.RouteCost(best_route)
        
        size = len(best_route)
        
        improve = 0

        while improve < max_iteration:
            best_cost = self.RouteCost(best_route)
            
            for i in range(1, size-1):
                for j in range(i+1, size):
                    new_route = self.TwOPTSwap(best_route, i,j)
                    new_cost = self.RouteCost(new_route)

                    if(new_cost < best_cost):
                        improve = 0
                        best_route = new_route
                        best_cost = new_cost
                                              
            
            improve += 1
        route[:] = best_route
            
    def GainSwap(self, x0_antecessor, x0, x0_sucessor, y0_antecessor, y0, y0_sucessor):
        del_distance = 0 ; add_distance = 0
            
        if(y0==x0_sucessor) or (x0_sucessor==y0_antecessor):
            del_distance = self.cost_matrix[x0_antecessor][x0] + self.cost_matrix[y0][y0_sucessor]
            add_distance = self.cost_matrix[x0_antecessor][y0] + self.cost_matrix[x0][y0_sucessor]
        
        elif(x0==y0_sucessor) or (y0_sucessor==x0_antecessor):
            del_distance = self.cost_matrix[y0_antecessor][y0] + self.cost_matrix[x0][x0_sucessor]
            add_distance = self.cost_matrix[y0_antecessor][x0] + self.cost_matrix[y0][x0_sucessor]
        
        else:
            del_distance = self.cost_matrix[x0_antecessor][x0] + self.cost_matrix[x0][x0_sucessor] + self.cost_matrix[y0_antecessor][y0] + self.cost_matrix[y0][y0_sucessor]
            add_distance = self.cost_matrix[x0_antecessor][y0] + self.cost_matrix[y0][x0_sucessor] + self.cost_matrix[y0_antecessor][x0] + self.cost_matrix[x0][y0_sucessor]
        
        result = del_distance - add_distance
        return(result)
    
    def Swap(self, route):
        for i in range(1,len(route)-1):
            for j in range(i+1,len(route)-1):
                if(self.GainSwap(route[i-1],route[i],route[i+1],route[j-1],route[j],route[j+1])>0):
                    aux = route[i]
                    route[i] = route[j]
                    route[j] = aux





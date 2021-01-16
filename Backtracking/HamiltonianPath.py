class Hamilatonian:
    def __init__(self,adjancyMatrix):
        self.adjancyMatrix=adjancyMatrix
        self.num_of_vertexes=len(adjancyMatrix)
        self.hamilitonianPath=[None]*self.num_of_vertexes

    def hamilatonian_cycle(self):
        self.hamilitonianPath[0]=0

        if not self.hamilitonianPath[1]:
            print('no feasible solution..')
        else:
            self.show_hamilatonian_path()

    """ backtrack logic """
    def find_feasable_solution(self,postion):
        """ to check wether if we are done --> is the first vertex have the edge/connection with the last-node to form a cycle?"""
        if postion == self.num_of_vertexes:
            x=self.hamilitonianPath[postion-1] #to get last vertex ie c
            y=self.hamilitonianPath[0] #first vertex i.e a
            if self.adjancyMatrix[x][y] == 1 : return True
            else: return False
        for vertex_index in range(1,self.num_of_vertexes):
            if self.is_feasible(vertex_index,postion):
                self.hamilitonianPath[postion] = vertex_index

                if self.find_feasable_solution(postion+1): return True
                # BACKTRACK IF THERES NO FEASIBLE SOLN IN POS+1 TO POS
            return False

    def is_feasible(self,vertex,actual_position):
        # case 1 : wether theres conection b/w two vertex,if it is then cell ? 1 : 0
        if self.adjancyMatrix[self.hamilitonianPath[actual_position-1]][vertex] == 0:
            return False

        # case 2: wether we have already visited/added the vertex in path list
        for i in range(actual_position):
            if self.hamilitonianPath[i] == vertex: return False

        return True

    def show_hamilatonian_path(self):
        print("Hamilatonian path exists")

        for i in range(self.num_of_vertexes):
            print(self.hamilitonianPath[i]) #will print the vertex as 1

        print(self.hamilitonianPath[0])

if __name__ == "__main__":
    adjancy_matrix=[[0,1,0],
                    [1,0,1],
                    [1,1,0]
                    ] #forms triangle
    hamil=Hamilatonian(adjancy_matrix)
    hamil.hamilatonian_cycle()










""" to set the color in the vertexes such that there ajacent vertex does not have the same color  """

class Colouring_prob:
    def __init__(self,num_vertices,num_colors,grap_matrix):
        self.num_vertices=num_vertices
        self.num_colors=num_colors
        self.colors=[0]*num_vertices
        self.grap_matrix=grap_matrix

    def solving_problem(self):
        if self.solve(0):
            self.show_result()
        else:
            print('theres feasible solution')

    def solve(self,node_index):
        if node_index == self.num_vertices:
            return True

        # try all colors with list of colors
        for color_index in range(1,self.num_colors+1):
            if self.is_color_valid(node_index,color_index):
                # will set the current color in that node_index
                self.colors[node_index]=color_index

            # check for next node_index
            if self.solve(node_index+1):
                return True

            # BACKTRACK
        return False

    def is_color_valid(self,node_index,color_index):
        for i in range(self.num_vertices):
            """ check wether theres connection with adjancent node and the color of curr_node not equals to  adjancent node  """
            if self.grap_matrix[node_index][i] == 1 and color_index==self.colors[i]:
                return False
        return True

    def show_result(self):
        for i in range(self.num_vertices):
            print('node %d as color index: %d' % (i,self.colors[i]))

if __name__ == "__main__":
    grapMatrix=[[0,1,0,1,0],
                [1,0,1,0,1],
                [0,1,0,1,0],
                [1,1,1,0,1],
                [0,0,0,1,0],
    ]
    num_colors=3
    num_vertices=5

    colorin_problem=Colouring_prob(num_vertices,num_colors,grapMatrix)
    colorin_problem.solving_problem()
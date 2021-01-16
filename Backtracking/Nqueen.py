class NqueenProblem:

    def __init__(self,num_of_queen):
        self.num_of_queen=num_of_queen
        self.chess_table=[[None for i in range(num_of_queen)] for j in range(num_of_queen)]

    def solveQueenProblem(self):

        if self.solve(0):
            self.printQueens()
        else:
            print('no solution...')

    def solve(self,col_index):
        if col_index==self.num_of_queen:
            return True

        for row_index in range(self.num_of_queen):

            if self.isPlaceValid(row_index,col_index):
                self.chess_table[row_index][col_index]=1

                if self.solve(col_index+1):
                    return True
                # when there no more column left to place the queen
                # backtrack


                self.chess_table[row_index][col_index]=0
        return False

    def isPlaceValid(self,row_index,col_index):
        # case--> when two queens are placed in same row
        for i in range(col_index):
            if self.chess_table[row_index][i] == 1:
                return False

        # case-->diagonally from top-left to bottom-right
        j=col_index
        for i in range(row_index,-1,-1):
            if j<0:
                break
            if self.chess_table[i][j] == 1:
                return False
            j=j-1


        # case-->diagonally from top-right to bottom-left
        j=col_index
        for i in range(row_index,len(self.chess_table)):
            if j<0:
                break
            if self.chess_table[i][j] == 1:
                return False
            j=j-1

        return True

    def printQueens(self):
        for i in range(self.num_of_queen):
            for j in range(self.num_of_queen):

                if self.chess_table[i][j] == 1:
                    print(" # ",end="")
                else:
                    print(" - ",end="")

            print('\n')




if __name__ == "__main__":
    queenProb=NqueenProblem(10)
    queenProb.solveQueenProblem()



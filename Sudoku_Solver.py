# encoding: utf-8
#*********************************************************************************************************************** Sudoku_Solver.py
"""Sudoku_Solver.py
"""

#***********************************************************************************************************************

#======================================================================================================================= Imports

#======================================================================================================================= Static

#======================================================================================================================= Classes
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        row = [0] * 9
        col = [0] * 9
        sqr = [0] * 9

        pos_to_sqr = {}
        empty_pos = []

        def _isValid(i, j, num):
            if row[i] & 1<<num:
                return False

            if col[j] & 1<<num:
                return False

            if sqr[pos_to_sqr[(i,j)]] & 1<<num:
                return False

            return True


        def _fill(pos_i):
            if pos_i == len(empty_pos):
                return True

            for k in range(pos_i, len(empty_pos)):
                i = empty_pos[k][0]
                j = empty_pos[k][1]
                for num in range(1, 10):
                    if _isValid(i,j, num):
                        board[i][j] = str(num)
                        row[i] |= 1 << num
                        col[j] |= 1 << num
                        sqr[pos_to_sqr[(i,j)]] |= 1 << num

                        if _fill(pos_i + 1):
                            return True

                        row[i] ^= 1 << num
                        col[j] ^= 1 << num
                        sqr[pos_to_sqr[(i,j)]] ^= 1 << num

                return False

        #scan the board
        for i in range(9):
            for j in range(9):
                k = pos_to_sqr.setdefault((i,j),(i / 3) * 3 + j / 3)
                if board[i][j] != '.':
                    num = int(board[i][j])
                    row[i] |= 1 << num
                    col[j] |= 1 << num
                    sqr[k] |= 1 << num
                else:
                    empty_pos.append((i,j))

        #fill empties
        _fill(0)


#======================================================================================================================= Functions

#***********************************************************************************************************************

if __name__ == '__main__':
    solution = Solution()
    board = [list("..9748..."),list("7........"),list(".2.1.9..."),list("..7...24."),list(".64.1.59."),list(".98...3.."),list("...8.3.2."),list("........6"),list("...2759..")]
    solution.solveSudoku(board)
    print board
    #***********************************************************************************************************************
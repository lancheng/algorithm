# encoding: utf-8
#*********************************************************************************************************************** matrix_spirally_shift.py
"""matrix_spirally_shift.py
"""

#***********************************************************************************************************************

#======================================================================================================================= Imports

#======================================================================================================================= Static

#======================================================================================================================= Classes
class Solution:
    def shift_clockwise(self, matrix):
        l = len(matrix)

        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        o_x = 0  # o_x <= (l - 1) / 2
        o_y = 0

        cur_x = o_x
        cur_y = o_y
        cur = matrix[cur_x][cur_y]
        d = 0

        while o_x <= (l - 1) / 2 and l - o_x - 1 > o_x:
            next_x = cur_x + direction[d][0]
            next_y = cur_y + direction[d][1]

            if next_x < o_x or next_y < o_y or next_x > (l - o_x - 1) or next_y > (l - o_y - 1):
                d = (d + 1) % 4
                next_x = cur_x + direction[d][0]
                next_y = cur_y + direction[d][1]

            temp = matrix[next_x][next_y]
            matrix[next_x][next_y] = cur
            cur = temp

            cur_x = next_x
            cur_y = next_y

            if cur_x == o_x and cur_y == o_y:
                o_x += 1
                o_y += 1
                d = 0
                cur_x = o_x
                cur_y = o_y
                cur = matrix[cur_x][cur_y]


#======================================================================================================================= Functions

#***********************************************************************************************************************

if __name__ == '__main__':
    matrix = []

    l = int(raw_input())
    for i in range(l):
        row = raw_input().split()
        if len(row) != l:
            print 'Error'
            raise

        matrix.append(row)

    Solution().shift_clockwise(matrix)
    print matrix


    #***********************************************************************************************************************
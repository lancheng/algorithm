# encoding: utf-8
#*********************************************************************************************************************** string_valid_parentheses.py
"""string_valid_parentheses.py
"""

#***********************************************************************************************************************

#======================================================================================================================= Imports

#======================================================================================================================= Static

#======================================================================================================================= Classes
class Solution:
    def check_valid_parenthese(self, str):
        count = 0
        total = 0
        for c in str:
            if c == '(':
                count += 1
            else:
                count -= 1
                total += 1

            if count < 0:
                break

        return total if count == 0 else False


#====================================================================================
# ================================== Functions

#***********************************************************************************************************************

if __name__ == '__main__':
    while True:
        print Solution().check_valid_parenthese(raw_input())

    #***********************************************************************************************************************
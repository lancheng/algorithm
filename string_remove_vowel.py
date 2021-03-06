# encoding: utf-8
#*********************************************************************************************************************** string_remove_vowel.py
"""string_remove_vowel.py
"""

#***********************************************************************************************************************

#======================================================================================================================= Imports

#======================================================================================================================= Static

#======================================================================================================================= Classes
class Solution:

    vowel = 'aeiouAEIOU'

    def __init__(self,str):
        self.str = str

    def remove_vowel(self):
        result = ''
        for c in self.str:
            if not c in self.vowel:
                result += c

        return result


#======================================================================================================================= Functions

#***********************************************************************************************************************

if __name__ == '__main__':
    print Solution(raw_input()).remove_vowel()

    #***********************************************************************************************************************
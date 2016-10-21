# encoding: utf-8
#*********************************************************************************************************************** string_longest_palindromic_string.py
"""string_longest_palindromic_string.py
"""

#***********************************************************************************************************************

#======================================================================================================================= Imports

#======================================================================================================================= Static

#======================================================================================================================= Classes
class Solution:
    def _is_palindromic(self,str, start, end):
        if start > end:
            return False

        mid = start + (end - start) / 2

        for i in xrange(mid - start + 1):
            if str[start + i] != str[end - i]:
                return False

        return True

    def get_longest_palindromic_substring_I(self, str):
        max_len = 0
        str_len = len(str)
        p_end = 0

        for i in xrange(str_len):
            if self._is_palindromic(str, i - max_len, i):
                p_end = i
                max_len += 1
            elif i - max_len - 1 >= 0 and self._is_palindromic(str, i - max_len - 1, i):
                p_end = i
                max_len += 2

        return max_len, str[p_end - max_len + 1: p_end + 1]




#======================================================================================================================= Functions

#***********************************************************************************************************************

if __name__ == '__main__':
    while True:
        print Solution().get_longest_palindromic_substring_I(raw_input())

    #***********************************************************************************************************************
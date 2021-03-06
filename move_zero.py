# encoding: utf-8
#*********************************************************************************************************************** move_zero.py
"""move_zero.py
"""

#***********************************************************************************************************************

#======================================================================================================================= Imports

#======================================================================================================================= Static

#======================================================================================================================= Classes
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        first_zero_pos = -1
        length = len(nums)
        for i in xrange(length):
            if nums[i] != 0 and first_zero_pos >= 0:
                temp = nums[i]
                nums[i] = nums[first_zero_pos]
                nums[first_zero_pos] = temp
                first_zero_pos += 1
            elif nums[i] == 0 and first_zero_pos == -1:
                first_zero_pos = i

#======================================================================================================================= Functions

#***********************************************************************************************************************

if __name__ == '__main__':
    pass

    #***********************************************************************************************************************
# encoding: utf-8
#*********************************************************************************************************************** reverse_list.py
"""reverse_list.py
"""

#***********************************************************************************************************************

#======================================================================================================================= Imports
import time
#======================================================================================================================= Static

#======================================================================================================================= Classes
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is not None:
            old_head = head.next
            new_head = head

            while old_head is not None:
                temp = old_head
                old_head = old_head.next

                temp.next = new_head
                new_head = temp

            head = new_head

        return head

#======================================================================================================================= Functions

#***********************************************************************************************************************

if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)

    node1.next = node2

    solution = Solution()

    start = time.time()
    solution.reverseList(node1).val
    print time.time() - start



#***********************************************************************************************************************
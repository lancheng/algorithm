# encoding: utf-8
#*********************************************************************************************************************** invert_binary_string.py
"""invert_binary_string.py
   LeetCode OJ #226
"""

#***********************************************************************************************************************

#======================================================================================================================= Imports

#======================================================================================================================= Static

#======================================================================================================================= Classes
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree_Recursive(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is not None:
            temp = root.right
            root.right = root.left
            root.left = temp

            self.invertTree(root.left)
            self.invertTree(root.right)

        return root

    def invertTree_Iterative(self,root):
        from collections import deque
        if root is not None:
            treeQ = deque() #deque is efficient to pop nodes from both ends, while list is slow to pop nodes from its the beginning.
            treeQ.append(root)

            while len(treeQ) > 0:
                node = treeQ.popleft()
                if node is not None:
                    temp = node.right
                    node.right = node.left
                    node.left = temp

                    treeQ.append(node.right)
                    treeQ.append(node.left)

        return root

#======================================================================================================================= Functions

#***********************************************************************************************************************

if __name__ == '__main__':
    pass

    #***********************************************************************************************************************
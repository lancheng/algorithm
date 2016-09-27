# encoding: utf-8
#*********************************************************************************************************************** LCA.py
"""LCA.py
    Lowest Common Ancestor of a Binary Search Tree
    LeetCode OJ 235
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
    def lowestCommonAncestor_1(self, root, p, q):
        """
        this algorithm may have problems if p or q does not exist in the BST but there is a node's value between them.
        :param root:
        :param p:
        :param q:
        :return:
        """
        while root is not None:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                break

        return root
    def lowestCommonAncestor_2(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        p_found, path_p = self.find(root, p)
        q_found, path_q = self.find(root, q)

        if p_found and q_found:
            length = min(len(path_p),len(path_q))
            for i in range(0, length):
                if path_p[i] != path_q[i]:
                    return path_p[i-1]
            return path_p[length-1]

        return None

    def find(self, root, num):
        result = list()

        node = root
        is_found = False
        while node is not None:
            result.append(node)
            if num.val == node.val:
                is_found = True
                break

            if num.val > node.val:
                node = node.right
            else:
                node = node.left

        return is_found, result


#======================================================================================================================= Functions

#***********************************************************************************************************************

if __name__ == '__main__':
    pass

    #***********************************************************************************************************************
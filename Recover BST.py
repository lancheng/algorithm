# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        #Morris Traverse
        first = None
        second = None
        prev = None
        
        cur_node = root
        while cur_node:
            if not cur_node.left:
                if prev and prev.val > cur_node.val:
                    if not first:
                        first = prev

                    second = cur_node
                prev = cur_node
                cur_node = cur_node.right
            else:
                tmp = cur_node.left
                while tmp.right and tmp.right != cur_node:
                    tmp = tmp.right
                
                if not tmp.right:
                    tmp.right = cur_node
                    cur_node = cur_node.left
                else:
                    if prev and prev.val > cur_node.val:
                        if not first:
                            first = prev
                        
                        second = cur_node
                    
                    prev = cur_node

                    tmp.right = None
                    cur_node = cur_node.right
        
        first.val, second.val = second.val, first.val


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    print root.val
    solution.recoverTree(root)
    print root.val
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    tree_paths = []
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        current_path = ''
        self.dfs(root, current_path)

        return Solution.tree_paths

    def dfs(self, tree_node, current_path):
        if tree_node is None:
            return

        current_path = len(current_path) and '->'.join([current_path, str(tree_node.val)]) or str(tree_node.val)

        if tree_node.left is None and tree_node.right is None:
            self.tree_paths.append(current_path)

        self.dfs(tree_node.left,current_path)
        self.dfs(tree_node.right,current_path)

if __name__ == '__main__':
    solution = Solution()

    root = TreeNode(1)
    root.left = TreeNode(2)

    solution.binaryTreePaths(root)

    #***********************************************************************************************************************
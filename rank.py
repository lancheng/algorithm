# Design an data structure. it has two functions:
# accept(x), where x is an integer and add x to the data structure
# rank(x), which return the count of numbers which are less than x.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.root = None

    def accept(self, x):
        self.root = self._insert(self.root, x)

    # Insert a node to a None kid
    # This is a O(lgN) operation
    # This method will not guarantee this BST is balanced
    def _insert(self, node, x):
        if not node:
            return TreeNode(x)

        if x <= node.val:
            node.left = self._insert(node.left, x)
        else:
            node.right = self._insert(node.right, x)

        return node

    def _get_num(self, node):
        if not node:
            return 0

        return self._get_num(node.left) + self._get_num(node.right) + 1

    def _rank(self, x, node):
        if not node:
            return 0

        if x <= node.val:
            return self._rank(x, node.left)
        else:
            return 1 + self._get_num(node.left) + self._rank(x, node.right)

    def rank(self, x):
        return self._rank(x, self.root)

if __name__ == '__main__':
    s = Solution()
    s.accept(1)
    s.accept(4)
    s.accept(-1)
    s.accept(2)
    s.accept(2)

    print s.rank(2)

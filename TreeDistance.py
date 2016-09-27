class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Tree:
    def _create_tree(self, node, num):
        if not node:
            return TreeNode(num)

        if num < node.val:
            node.left = self._create_tree(node.left, num)
        else:
            node.right = self._create_tree(node.right, num)

        return node

    def __init__(self, l):
        self.root = None

        for i in range(len(l)):
            self.root = self._create_tree(self.root, int(l[i]))

    def _get_lca(self, node, num1, num2):
        if not node:
            return None

        if num1 < node.val and num2 < node.val:
            return self._get_lca(node.left, num1, num2)

        if num1 > node.val and num2 > node.val:
            return self._get_lca(node.right, num1, num2)

        return node

    def _get_depth(self, node, num1):
        if not node:
            return -1

        if num1 == node.val:
            return 0

        if num1 < node.val:
            depth = self._get_depth(node.left, num1)
        else:
            depth = self._get_depth(node.right, num1)

        return depth + 1 if depth != -1 else -1


    def get_distance(self, num1, num2):
        node = self._get_lca(self.root, num1, num2)

        if not node:
            raise

        depth1 = self._get_depth(node, num1)
        depth2 = self._get_depth(node, num2)

        if -1 in (depth1, depth2):
            raise

        return depth1 + depth2

if __name__ == '__main__':
    import sys
    l = raw_input().split()

    tree = Tree(l)

    try:
        num1 = int(raw_input())
        num2 = int(raw_input())
        print tree.get_distance(num1, num2)
    except:
        print 'Wrong to get distance'









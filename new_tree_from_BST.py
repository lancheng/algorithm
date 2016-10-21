# -*- coding: utf-8 -*-
'''给我一个BST,要求得到一颗新树,每个节点的内容是比此节点的元素值大的元素的总和。
我一看不会,赶紧想,就说用stack去做,然后他说为什么不对每个点分别 求,还给我一个函数原型,
我说不要,这样重复计算,我用stack可以n做出来,他说那你 写,我写啊写,写好了,他说不明白,给解释了很久,最后他终于明白了,简直要哭。
这里 我明白一个道理,你要是解法和面试官不一样,他们很多时候就懵了,也不好意思说看不懂,然后很长时间就在怀疑你。
不过,面试后遇到cmu女神,她说这题见过,递归就行了, 我听着就泪奔了,还是要多训练,差距太大.'''

class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def create_new_tree(self, node, s):
        if not node:
            return None

        new_right = self.create_new_tree(node.right, s)

        right_sum = self.get_sum(node.right)

        new_node = TreeNode(right_sum + s)
        new_left = self.create_new_tree(node.left, new_node.val + node.val)

        new_node.left = new_left
        new_node.right = new_right

        return new_node

    def get_sum(self, node):
        if not node:
            return 0

        return node.val + self.get_sum(node.left) + self.get_sum(node.right)

def add_to_tree(node, val):
    if not node:
        return TreeNode(val)

    if val < node.val:
        node.left = add_to_tree(node.left, val)
    else:
        node.right = add_to_tree(node.right, val)

    return node

if __name__ == '__main__':
    root = None
    l = map(int, raw_input().split())

    for n in l:
        root = add_to_tree(root, n)

    new_root = Solution().create_new_tree(root, 0)
    print new_root


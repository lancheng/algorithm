from collections import deque
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# the following code lists nodes for one specified level
# depth starts from 1.
def list_nodes_at_depth(root, depth):
    result = []
    
    if root:
        tree_q = deque()
        tree_q.append(root)
        level = 0

        while tree_q:
            level += 1
            next_level = deque()
            while tree_q:
                node = tree_q.popleft()
                if level == depth:
                    result.append(node.val)
                else:
                    if node.left:
                        next_level.append(node.left)
                    if node.right:
                        next_level.append(node.right)

            if level == depth:
                return result

            tree_q = next_level

    return result


# the follwing code lists all nodes according to their depth
def dfs(node, depth, result):
    if not node:
        return

    if len(result) == depth:
        result.append([])

    result[depth].append(node.val)
    dfs(node.left, depth + 1, result)
    dfs(node.right, depth + 1, result)


def list_nodes_by_depth(root):
    result = []
    dfs(root, 0, result)
    return result

#following code is used to test
if __name__ == '__main__':
    def str2tree(s):
        def _to_node():
            val = tree_str.next()
            if val != '#':
                node = TreeNode(int(val))
                node.left = _to_node()
                node.right = _to_node()
                return node
            return None

        tree_str = iter(s.split())
        return _to_node()
    ''' pre-order dfs for the following tree:
                1
               / \
              2   6
             /\   /\  
            3  # #  #
           /\
          4  #
         /\
        #  5
           /\
          #  #
    '''
    tree = "1 2 3 4 # 5 # # # # 6 # #" 
    root = str2tree(tree)
    print list_nodes_by_depth(root)
    print list_nodes_at_depth(root, 3)


        


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        def dfs(node):
            if not node:
                return None
            cp =Node(node.val)
            for child in node.children:
                cp.children.append(dfs(child))
            return cp
        return dfs(root) if root else None
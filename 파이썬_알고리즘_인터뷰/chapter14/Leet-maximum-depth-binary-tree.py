import collections
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth( root: Optional[TreeNode]) -> int:
    if root is None:
        return 0

    queue = collections.deque(root)
    depth = 0

    while queue:
        depth += 1
        for _ in range(len(queue)):
            cur_root = queue.popleft()
            print(cur_root)
            if cur_root.left:
                print("?")

maxDepth([3,9,20,None,None,15,7])
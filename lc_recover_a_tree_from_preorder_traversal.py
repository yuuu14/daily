from typing import (
    List,
    Tuple,
    Optional,
)
from collections import (
    Counter,
    deque,
)
import re

from lc_py_tools import (
    TreeNode,
    BinaryTree,
)


class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        # example: traversal = "1-2--3--4-5--6--7"
        nodes = re.split("[-]+", traversal)
        nodes = list(map(int, nodes))
        root = TreeNode(nodes[0])
        nodes = nodes[1:]
        nodes_len = len(nodes)
        findall_dashes = re.findall("[-]+", traversal)
        depths = list(map(lambda x: len(x), findall_dashes))
        # if next_depth = cur_depth + 1, add left/right child
        # if not, go back to root
        def dfs(
            parent: TreeNode | None = None, 
            depth: int = 0, 
            index: int = 0
        ) -> int:
            if index >= nodes_len or index == -1:
                return -1
            if index and depths[index] <= depth:
                # end of current subtree
                return index
            child = TreeNode(nodes[index])
            if not parent.left:
                parent.left = child
                next_index = dfs(parent.left, depth + 1, index + 1)
                return dfs(parent, depth, next_index)
            else:
                parent.right = child
                return dfs(parent.right, depth + 1, index + 1)

            
        dfs(root, 0)

        return root
    
    def __call__(self, foo: callable, **kwargs: dict):
        return foo(**kwargs)
        

def main():
    solution = Solution()

    args = dict(
        traversal = "1-2--3--4-5--6--7"
    )
    results = solution(solution.recoverFromPreorder, **args)
    print(results)


if __name__ == "__main__":
    main()







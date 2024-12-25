from typing import (
    List,
    Tuple,
    Optional,
)

from lc_py_tools import (
    TreeNode,
    BinaryTree,
)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # root = [1,3,2,5,3,None,9]
        if not root:
            return []
        q = deque([root, "$"])
        max_values = []
        same_level_vals = []
        while q:
            fr = q.popleft()
            if fr == "$":
                max_values.append(max(same_level_vals))
                same_level_vals = []
                if q:
                    q.append("$")
                continue
            same_level_vals.append(fr.val)
            if fr.left:
                q.append(fr.left)
            if fr.right:
                q.append(fr.right)
        return max_values
        Ellipsis

    def __call__(self, foo: callable, **kwargs: dict):
        return foo(**kwargs)


def main():
    solution = Solution()

    root = [1,3,2,5,3,None,9]

    args = dict(
        root=BinaryTree.build_binary_tree(root),
    )
    results = solution(solution.largestValues, **args)
    print(results)


if __name__ == "__main__":
    main()


from typing import (
    List,
    Any,
    Optional,
)
from collections import deque
from dataclasses import dataclass


# Binary Tree
@dataclass
class TreeNode:
    val: int = 0
    left: Any = None
    right: Any = None


class BinaryTree:

    @staticmethod
    def build_binary_tree(tree_list: List) -> Optional[TreeNode]:
        if not tree_list or tree_list[0] is None:
            return None
        root = TreeNode(tree_list[0])
        queue = deque([root])
        i = 1
        while i < len(tree_list):
            node = queue.popleft()
            if tree_list[i] is not None:
                node.left = TreeNode(tree_list[i])
                queue.append(node.left)
            i += 1
            if i < len(tree_list):
                if tree_list[i] is not None:
                    node.right = TreeNode(tree_list[i])
                    queue.append(node.right)
                i += 1
        return root

    @staticmethod
    def print_binary_tree(root: TreeNode):
        if root is None:
            return []
        queue = deque([root])
        res = []
        while queue:
            node = queue.popleft()
            if node is None:
                res.append(None)
                continue
                
            res.append(node.val)
            if node.right:
                queue.append(node.left)
                queue.append(node.right)

            elif node.left:
                queue.append(node.left)
        return res
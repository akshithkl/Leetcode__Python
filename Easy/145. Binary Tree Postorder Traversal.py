# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        stack = [(root, False)]
        res = []

        while stack:
            node, visited = stack.pop()
            
            if node:
                if visited:
                    res.append(node.val)  # Add to result after children
                else:
                    # Postorder: left -> right -> root
                    stack.append((node, True))          # Add root after children
                    stack.append((node.right, False))   # Right child
                    stack.append((node.left, False))    # Left child

        return res

# | Metric               | Value                                |
# | -------------------- | ------------------------------------ |
# | **Time Complexity**  | `O(n)`                               |
# | **Space Complexity** | `O(n)` (stack + result list)         |
# | **Approach**         | Iterative using Stack + Visited Flag |
# | **Traversal Type**   | Postorder (Left → Right → Root)      |

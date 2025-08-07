# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        total = 0
        if root.left:
            if not root.left.left and not root.left.right:
                total += root.left.val
            else:
                total += self.sumOfLeftLeaves(root.left)

        total += self.sumOfLeftLeaves(root.right)

        return total

# | Component             | Description                    |
# | --------------------- | ------------------------------ |
# | **Algorithm**         | Depth-First Search (DFS)       |
# | **Technique**         | Recursion + Tree Traversal     |
# | **Time Complexity**   | O(n)                           |
# | **Space Complexity**  | O(h), where h = height of tree |
# | **Type of Traversal** | Pre-order style DFS            |

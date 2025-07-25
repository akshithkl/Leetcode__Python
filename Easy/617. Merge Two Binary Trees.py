# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root1 and not root2:
            return None
        
        v1 = root1.val if root1 else 0
        v2 = root2.val if root2 else 0
        root = TreeNode(v1 + v2)

        root.left = self.mergeTrees(root1.left if root1 else None, root2.left if root2 else None)
        root.right = self.mergeTrees(root1.right if root1 else None , root2.right if root2 else None)
    
        return root



# | **Aspect**           | **Value**                                                                     |
# | -------------------- | ----------------------------------------------------------------------------- |
# | **Algorithm**        | Recursive Tree Traversal                                                      |
# | **Approach**         | Top-Down Recursive Merge                                                      |
# | **Technique**        | Depth-First Search (DFS) – Preorder style                                     |
# | **Time Complexity**  | `O(min(n1, n2))` where `n1` and `n2` are the number of nodes in root1, root2  |
# | **Space Complexity** | `O(min(h1, h2))` due to recursion stack, where `h1` and `h2` are tree heights |
# | **Problem Type**     | Binary Tree Construction / Manipulation                                       |
# | **In-place?**        | No, creates a **new** merged tree                                             |
# | **Optimizable?**     | Tail recursion optimization (but Python does not support it natively)         |

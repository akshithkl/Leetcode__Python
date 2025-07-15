# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, MaxVal):
            if not node:
                return 0
            
            res = 1 if node.val >= MaxVal else 0
            MaxVal = max(node.val, MaxVal)
            res += dfs(node.left, MaxVal)
            res += dfs(node.right, MaxVal)
            return res
        
        return dfs(root, root.val)

# | Aspect               | Value                                        |
# | -------------------- | -------------------------------------------- |
# | **Algorithm**        | DFS (Depth-First Search)                     |
# | **Approach**         | Recursive Tree Traversal                     |
# | **Technique**        | Top-Down DFS with state propagation (MaxVal) |
# | **Time Complexity**  | O(n), where n is the number of nodes         |
# | **Space Complexity** | O(h), where h is the height of the tree      |
# | **Best Case**        | O(log n), for a balanced tree (space-wise)   |
# | **Worst Case**       | O(n), for a skewed tree (space-wise)         |


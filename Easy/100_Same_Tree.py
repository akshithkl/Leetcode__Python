# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        if not p and not q:
            return True
        
        if not p or not q or p.val != q.val:
            return False
        
        return (self.isSameTree(p.left, q.left) and 
               (self.isSameTree(p.right, q.right)) )
        

#  Time Complexity: O(n)

# You visit each node once.

# n is the total number of nodes in either tree (whichever is smaller if unequal).

# Space Complexity: 
#     O(h) in the best/average case, where h is the height of the tree (for recursion stack).

# In the worst case (skewed tree), h = n, so space complexity becomes O(n).

# In the best case (balanced tree), h = log n, so space becomes O(log n).

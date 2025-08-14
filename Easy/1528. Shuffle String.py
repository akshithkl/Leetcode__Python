class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        if len(s) != len(indices):
            return 
        res = [0] * len(s)
        for ch, i in zip(s, indices):
            res[i] = ch

        return "".join(res)

# Time complexity = O(n)
# Space complexity = O(n)
            
            

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       i = 0
       visited = {}
       result = 0
       for j in range(len(s)):
        if s[j] in visited:
            i = max(visited[s[j]],i)
        
        result = max(j -i + 1,result)
        visited[s[j]] = j+1
       return result

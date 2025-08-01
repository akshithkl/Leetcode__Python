class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = {}
        
        # Count the frequency of each character
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        
        length = 0
        odd_found = False
        
        for count in freq.values():
            if count % 2 == 0:
                length += count
            else:
                length += count - 1
                odd_found = True
        
        if odd_found:
            length += 1  # add one odd letter in the center
            
        return length


# | Aspect               | Value                                 |
# | -------------------- | ------------------------------------- |
# | **Technique**        | Greedy + Hashing (frequency counting) |
# | **Time Complexity**  | O(n)                                  |
# | **Space Complexity** | O(1) or O(k) where k ≤ 52             |

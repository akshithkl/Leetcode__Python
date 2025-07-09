class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Step 1: Initialize frequency array for 26 letters
        freq = [0] * 26
        
        # Step 2: Count each character manually
        for char in s:
            index = ord(char) - ord('a')  # Convert char to index 0-25
            freq[index] += 1
        
        # Step 3: Find the first unique character
        for i in range(len(s)):
            index = ord(s[i]) - ord('a')
            if freq[index] == 1:
                return i
        
        return -1

# Time: O(n) — Two passes through the string.
# Space: O(1) — Only 26-sized array (constant space for lowercase letters).

# | Technique               | Description                                                                |
# | ----------------------- | -------------------------------------------------------------------------- |
# | **Hashing (via Array)** | Use an array to simulate a hash table for character frequency (`a` to `z`) |
# | **Two-pass Scan**       | First pass to count, second pass to find the first unique                  |
# | **ASCII Mapping**       | Use `ord(char) - ord('a')` to convert char to index                        |

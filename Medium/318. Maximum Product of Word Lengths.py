class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        masks, lengths = [0]*n, [0]*n

        for i, word in enumerate(words):
            mask = 0
            for ch in word:
                mask |= 1 << (ord(ch) - ord('a'))   # set bit for character
            masks[i] = mask
            lengths[i] = len(word)

        res = 0
        for i in range(n):
            for j in range(i+1, n):
                if masks[i] & masks[j] == 0:  # no common characters
                    res = max(res, lengths[i] * lengths[j])
        return res


# | Aspect | Details |
# | ----------------------- | ----------------------------------------------------------------------------------------- |
# | Algorithm Technique | Brute force pair comparison with Bitmasking to check common characters efficiently |
# | Time Complexity | O(n² + nL) → O(nL) to build masks, O(n²) for pairwise comparisons (& is O(1)) |
# | Space Complexity | O(n) → store bitmasks and lengths for all words |

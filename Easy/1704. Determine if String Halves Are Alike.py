class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set("aeiouAEIOU")
        n = len(s)
        a, b = s[:n//2], s[n//2:]

        def count_vowels(sub):
            count = 0
            for ch in sub:
                if ch in vowels:
                    count += 1
            return count

        return count_vowels(a) == count_vowels(b)

# Time Complexity: O(n) → We scan through the string once.
# Space Complexity: O(1) → Only storing a fixed set of vowels.

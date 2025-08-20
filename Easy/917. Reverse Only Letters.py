class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = [i for i in s]
        l, r = 0, len(s)-1

        while l < r:
            if s[l].isalpha() and s[r].isalpha():
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            elif not s[l].isalpha():
                l += 1
            else:
                r -= 1
        return ''.join(s)

# | Aspect               | Details                                                              |
# | -------------------- | -------------------------------------------------------------------- |
# | **Algorithm**        | Two-Pointer Technique                                                |
# | **Time Complexity**  | **O(n)** (each char checked once)                                    |
# | **Space Complexity** | **O(n)** (list copy of string)                                       |
# | **When to use**      | Best when you want in-place style reversal with minimal extra memory |

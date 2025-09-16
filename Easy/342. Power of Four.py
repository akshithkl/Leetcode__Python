class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        # check if power of two first
        if n & (n - 1) != 0:
            return False
        # check if (n-1) is divisible by 3
        return (n - 1) % 3 == 0


# | **Aspect**             | **Details**                                                                     |
# | ---------------------- | ------------------------------------------------------------------------------- |
# | **Algorithm**          | Bit Manipulation + Modulo Property                                              |
# | **Approach/Technique** | Check power of two, then check modulo trick                                     |
# | **Time Complexity**    | **O(1)**                                                                        |
# | **Space Complexity**   | **O(1)**                                                                        |
# | **Key Idea**           | Powers of 4 are subset of powers of 2, and `(n-1) % 3 == 0` holds only for them |

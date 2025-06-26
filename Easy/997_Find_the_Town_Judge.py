class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        trust_scores = [0] * (n + 1)

        for a, b in trust:
            trust_scores[a] -= 1  # a trusts someone
            trust_scores[b] += 1  # b is trusted by a

        for i in range(1, n + 1):
            if trust_scores[i] == n - 1:
                return i  # This is the judge
        return -1  # No judge found

# Time Complexity: O(N + T)
# O(T) to iterate over the trust array and update trust scores.

# O(N) to check each person’s trust score to find the judge.

# Here,

# N is the number of people

# T is the number of trust relationships

# Space Complexity: O(N)
# We use a list trust_scores of size n + 1 → takes O(N) space.


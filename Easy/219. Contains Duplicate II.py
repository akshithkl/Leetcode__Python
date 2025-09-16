class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_seen = {}

        for i, num in enumerate(nums):
            if num in last_seen and i - last_seen[num] <= k:
                return True
            last_seen[num] = i

        return False


# | **Aspect**             | **Details**                                                                |
# | ---------------------- | -------------------------------------------------------------------------- |
# | **Algorithm Approach** | Hash Map Lookup                                                            |
# | **Technique**          | Sliding Window (via index difference check)                                |
# | **Time Complexity**    | **O(n)** → one scan, each lookup/update in dict is O(1) average            |
# | **Space Complexity**   | **O(n)** → in worst case, all elements are unique and stored in dictionary |
# | **Key Idea**           | Track last index of each element, return early when difference ≤ k         |

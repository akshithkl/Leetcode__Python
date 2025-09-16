class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = 0
        slow = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                return slow 

# | **Aspect**             | **Details**                                                  |
# | ---------------------- | ------------------------------------------------------------ |
# | **Algorithm**          | Floyd’s Tortoise and Hare (Cycle Detection)                  |
# | **Approach/Technique** | Linked list cycle detection adapted for array                |
# | **Time Complexity**    | **O(n)** (at most 2 passes through array)                    |
# | **Space Complexity**   | **O(1)** (only pointers used, no extra structures)           |
# | **Key Idea**           | Treat indices as "next pointers" → cycle caused by duplicate |

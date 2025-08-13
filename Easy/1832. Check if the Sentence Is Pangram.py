class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        seen = set()
        for ch in sentence:
            if 'a' <= ch <= 'z':
                seen.add(ch)
                if len(seen) == 26:  # early exit
                    return True
        return len(seen) == 26


#Summary Table

#Aspect	Value

#Algorithm	Hash Set Character Tracking + Early Termination
#Time Complexity	O(n) worst, O(1) best
#Space Complexity	O(1)

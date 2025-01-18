class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people, key = lambda x: (-x[0], x[1]))
        for p in people:
            ans.insert(p[1], p)
        return ans

'''Initial List of Tuples:
[(-7, 0), (-4, 4), (-7, 1), (-5, 0), (-6, 1), (-5, 2)]

Compare (-7, 0) and (-4, 4):

First elements: -7 < -4, so (-7, 0) comes before (-4, 4).
Compare (-7, 0) and (-7, 1):

First elements: -7 == -7, so compare second elements: 0 < 1, so (-7, 0) comes before (-7, 1).
Compare (-7, 1) and (-5, 0):

First elements: -7 < -5, so (-7, 1) comes before (-5, 0).
Compare (-5, 0) and (-6, 1):

First elements: -5 > -6, so (-6, 1) comes before (-5, 0).
Compare (-5, 0) and (-5, 2):

First elements: -5 == -5, so compare second elements: 0 < 2, so (-5, 0) comes before (-5, 2).
Compare (-6, 1) and (-4, 4):

First elements: -6 < -4, so (-6, 1) comes before (-4, 4).
Fully Sorted List of Tuples:
After sorting based on the rules: [(-7, 0), (-7, 1), (-6, 1), (-5, 0), (-5, 2), (-4, 4)]

'''

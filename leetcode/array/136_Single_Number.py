from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for v, i in Counter(nums).items():
            if i == 1:
                return v
        

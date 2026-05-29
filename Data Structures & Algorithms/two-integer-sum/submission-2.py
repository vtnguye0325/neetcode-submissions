from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            d[nums[i]]=i 

        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in d and d[remainder] != i:
                return [i,d[remainder]]
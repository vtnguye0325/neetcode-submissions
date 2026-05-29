from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            remainder = target - nums[i]
            print(i)
            if remainder in d and d[remainder] != i:
                return [d[remainder],i]
            d[nums[i]]=i
                    
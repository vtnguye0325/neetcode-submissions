class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_nums = set()
        set_size = 0
        for num in nums:
            set_nums.add(num)
            if len(set_nums) == set_size:
                return True
            set_size +=1
        return False
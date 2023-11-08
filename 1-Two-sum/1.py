from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for index in range(0,len(nums)):

            transfer = target - nums[index]
            nums[index] = None

            if transfer in nums:
                
                return [index, nums.index(transfer)]
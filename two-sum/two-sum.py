from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for index_first in range(0,len(nums)):
            for index_second in range(0,len(nums)):
                
                if nums[index_first] + nums[index_second] == target:
                    return [index_first, index_second]
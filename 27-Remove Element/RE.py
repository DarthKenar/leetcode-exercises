class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
         
        removals = 0
        for i in range(len(nums)):
            if nums[i+removals] == val:
                nums.pop(i+removals)
                removals -= 1
        return len(nums)
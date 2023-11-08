from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxim = 0 
        i = 0
        j = len(height)-1
        while i < j:
            width = abs(i-j)
            area = width * min(height[i],height[j])
            maxim = max(area,maxim)
            if height[i] > height[j]:
                j -=1
            else:
                i +=1
        return maxim 
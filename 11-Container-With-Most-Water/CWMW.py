class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        reverse = height.copy()
        reverse.sort(reverse=True)
        output = 0

        for i in range(1,len(reverse)):

            index_one = height.index(reverse[i-1])
            
            try:
                
                index_two = len(height[:index_one]) + height[index_one+1:].index(reverse[i]) +1
                
            except:
                
                index_two = height[:index_one].index(reverse[i])

            lower = min(height[index_one],height[index_two])
            width = max(index_one, index_two) - min(index_one, index_two)
            max_water = width*lower
            
            if max_water > output:
                
                output = max_water
                
        return output



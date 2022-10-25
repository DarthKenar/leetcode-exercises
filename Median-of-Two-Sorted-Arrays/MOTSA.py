class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        for i in range(0, len(nums2)):

            nums1.append(nums2[i])
            
        nums1.sort()
        longitud = len(nums1)
        
        if longitud == 1:
            
            return nums1[0]
        
        elif longitud % 2 == 0:
            
            return ((nums1[int((longitud/2)-1)]+nums1[int(longitud/2)])/2)
        
        else:
            
            return (nums1[int(longitud//2)])
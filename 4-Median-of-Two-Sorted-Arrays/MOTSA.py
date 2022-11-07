class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        for i in range(0, len(nums2)):

            nums1.append(nums2[i])
            
        nums1.sort()
        lenght = len(nums1)
        
        if lenght == 1:
            
            return nums1[0]
        
        elif lenght % 2 == 0:
            
            return ((nums1[int((lenght/2)-1)]+nums1[int(lenght/2)])/2)
        
        else:
            
            return (nums1[int(lenght//2)])
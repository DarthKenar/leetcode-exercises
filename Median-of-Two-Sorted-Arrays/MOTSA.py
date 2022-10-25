class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        def comprobacion(longitud, lista):
            
            if longitud == 1:
                
                return(lista[0])
            
            elif longitud % 2 == 0: 
                
                return ((lista[int((longitud/2)-1)]+lista[int(longitud/2)])/2)
            
            else:
                
                return (lista[int(longitud//2)])
        
        len_nums1 = len(nums1)
        len_nums2 = len(nums2)
        
        if len_nums1 > 0 and len_nums2 == 0:
            
            return(comprobacion(len_nums1, nums1))
        
        elif len_nums2 > 0 and len_nums1 == 0:
            
            return(comprobacion(len_nums2,nums2))
        
        else:
            
            for i in range(0, len_nums2):
                
                nums1.append(nums2[i])
                nums1.sort()
                
            return comprobacion((len_nums1+len_nums2), nums1)
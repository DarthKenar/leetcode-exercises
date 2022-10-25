class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        def comprobacion(longitud, lista):
            #es par
            if longitud % 2 == 0: 
                
                return ((lista[longitud/2]+lista[(longitud/2)+1])/2)
                
            #es impar
            else:
                
                return (lista[longitud//2])
        
        len_nums1 = len(nums1)
        len_nums2 = len(nums2)
        
        if len_nums1 > 0 and len_nums2 == 0:
            
            comprobacion(len_nums1, nums1)
        
        elif len_nums2 > 0 and len_nums1 == 0:
            
            comprobacion(len_nums2,nums2)
        
        else:
            return ((comprobacion(len_nums1, nums1)+comprobacion(len_nums2,nums2)/2))
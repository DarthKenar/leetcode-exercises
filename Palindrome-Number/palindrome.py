from math import floor
from math import log10

class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False
        elif x == 0:
            return True
        else:

            array = []
            longitud = floor(log10(x)+1)

            for index in range(0, longitud):

                array.append(floor(x%10))
                x = floor(x/10)
                
            if array == array[::-1]:
                return(True)
            else:
                return(False)
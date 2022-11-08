class Solution:
    def reverse(self, x: int) -> int:
        
        def reverse(x):
            
            return int(str(x)[::-1])
        
        def check_valid_value(x):
            
            if x >= 2**31 or x <= -2**31:
                
                return 0
            
            else:
                
                return x
        
        if x > 0 and x <= 2**31:
            
            return check_valid_value(reverse(x))
        
        elif x < 0 and x >= -2**31:
            
            x = -x
            return check_valid_value(-1*(reverse(x)))
        
        else:
            
            return 0
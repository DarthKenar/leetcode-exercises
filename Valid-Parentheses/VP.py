class Solution:
    def isValid(self, s: str) -> bool:
        gate = " "
        counter = 0
        
        for element in s:
            
            if element is "]":
                
                if gate[-1] != "[":
                    return False
                else:
                    gate = gate[:-1]
                    counter -= 1
                    
            elif element is ")":
                
                if gate[-1] != "(":
                    return False
                else:
                    gate = gate[:-1]
                    counter -= 1
                    
            elif element is "}":
                
                if gate[-1] != "{":
                    return False
                else:
                    gate = gate[:-1]
                    counter -= 1
                    
            else:
                gate = gate + element
                counter += 1
        if counter > 0:
            return False
        else:
            return True
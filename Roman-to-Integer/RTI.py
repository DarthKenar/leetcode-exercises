class Solution:
    def romanToInt(self, s: str) -> int:
        single_roman = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        double_roman = {"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
        output = 0
        
        while len(s) > 0:
            if s[-2:] in double_roman:
                output += double_roman[s[-2:]]
                s = s[:-2]
            else:
                output += single_roman[s[-1:]]
                s = s[:-1]
        return output
    
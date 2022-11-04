class Solution:
    """"a better way to do this is revert the implemented system
    if check first the longest word instead of the smallest
    """
    #"HolaMundo"
    def longestPalindrome(self, s: str) -> str:

        lenght = len(s) #"HolaMunud"
        if s == s[::-1]: return s
        check = 1
        
        while True:
            
            for i in range(0,check):
                if s[i:lenght+i-check] == s[i:lenght+i-check][::-1]:
                    return s[i:lenght+i-check]
                    break
            check += 1



a = Solution()
print(a.longestPalindrome("abb"))



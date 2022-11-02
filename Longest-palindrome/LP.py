class Solution:
    """"a better way to do this is revert the implemented system
    if check first the longest word instead of the smallest
    """
    def longestPalindrome(self, s: str) -> str:
        palindrome = ""
        for i in range(len(s)):
            for j in range(len(s)):
                if s[0+j:2+j+i] == (s[0+j:2+j+i])[::-1]:
                    if len(palindrome) < len(s[0+j:2+j+i]):
                        palindrome = s[0+j:2+j+i]
                        
        return palindrome


a = Solution()
a.longestPalindrome("babad")


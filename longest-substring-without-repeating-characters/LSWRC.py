class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        #In case empty s
        if len(s) == 0: return 0

        substring = s[0]
        output = 0
        list_string = [s[0]]

        for i in range(1,len(s)):
            if s[i] not in substring:
                substring = substring + s[i]
            else:
                list_string.append(substring)
                substring = s[i]

        #if len(list_string) == 1: return len(s)

        for i in list_string:
            if len(i) > output:
                output = len(i)
        return(output)
a = Solution()
print(a.lengthOfLongestSubstring("aab"))
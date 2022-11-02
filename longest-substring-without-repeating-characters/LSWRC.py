class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0: return 0

        substring = s[0]
        output = 0
        list_string = [s[0]]
        s = s + s[-1]

        for i in range(1,len(s)):

            if s[i] not in substring:

                substring = substring + s[i]

            else:

                list_string.append(substring)
                substring = substring[substring.index(s[i])+1:] + s[i]

        for i in list_string:

            if len(i) > output:

                output = len(i)
                
        return(output)
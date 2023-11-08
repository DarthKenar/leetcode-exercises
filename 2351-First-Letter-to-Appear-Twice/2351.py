class Solution:
    def repeatedCharacter(self, s: str) -> str:
            
        for i in range(1, len(s)):
            for j in range(i-1, -1, -1):
                if s[i] == s[j]:
                    return(s[i]) 
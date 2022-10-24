class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if x[:round(len(x))] == x[round(len(x))::-1]:
            return True
        else:
            return False
        
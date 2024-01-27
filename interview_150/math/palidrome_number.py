class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        reversed_s = s[::-1]
        if s == reversed_s:
            return True
        return False

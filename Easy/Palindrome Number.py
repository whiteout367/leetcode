class Solution:
    def isPalindrome(self, x: int) -> bool:
        s_x = str(x)
        revers_x = s_x[::-1]
        return s_x == revers_x
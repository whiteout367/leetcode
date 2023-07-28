class Solution:
    def reverse(self, x: int) -> int:
        """
        Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

        Example 1:

        Input: x = 123
        Output: 321

        -2^31 <= x <= 2^31 - 1

        Result

        Runtime
        36ms
        Beats 97.74%of users with Python3

        Memory
        16.13mb
        Beats 93.98%of users with Python3
        """
        #check x is negative num
        negative = False
        if x < 0:
            x = x * -1
            negative = True

        s_x = str(x)
        result = 0
        x = 1

        for i in s_x:
            result += int(i) * x
            x *= 10
        if (2**31) * -1 > result or result > (2**31)-1:
            return 0
        else:
            if negative:
                return result *-1
            else:
                return result 
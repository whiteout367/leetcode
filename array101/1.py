class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = 0
        a = []
        for i in nums:
            if i == 1:
                result += 1
            else:
                a.append(result)
                result = 0
        a.append(result)
        return max(a)
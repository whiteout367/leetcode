class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sq_list = []
        for i in nums:
            sq_list.append(i ** 2)
        result = sorted(sq_list)
        return result
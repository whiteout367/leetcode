class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        """
        1 <= nums.length <= 5000
        0 <= nums[i] <= 5000
        
        Input: nums = [3,1,2,4]
        Output: [2,4,3,1]
        
        짝수 왼쪽, 홀수 오른쪽
        return => list
        """
        if len(nums) == 1: return nums
        
        x = 0
        y = len(nums) - 1
        result = [0 for _ in range(len(nums))]
        
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                result[x] = nums[i]
                x += 1
            else:
                result[y] = nums[i]
                y -= 1
                
        return result
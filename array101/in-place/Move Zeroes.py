class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        1 <= nums.length <= 104
        -231 <= nums[i] <= 231 - 1

        input = [0,1,0,3,12]
        output = [1,3,12,0,0]
        """
        result = [0 for _ in range(len(nums))]
        j = 0
        if 0 not in nums:
            nums = nums[0:]
            if len(nums) == 1:
                nums[0] = nums[0]
            
        else:
            for i in range(len(nums)):
                if nums[i] != 0:
                    result[j] = nums[i]
                    j += 1
        
        for x in range(len(nums)):
            nums[x] = result[x]
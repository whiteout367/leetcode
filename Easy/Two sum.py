class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Example 1:

        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
        Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

        2 <= nums.length <= 104
        -109 <= nums[i] <= 109
        -109 <= target <= 109

        합이 타켓인 경우의 인덱스를 찾는 문제(투포인터를 사용)(값이 안 나옴)
        그냥 이중 for문
        """
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return list((i,j))
            
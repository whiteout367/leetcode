class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        합이 타겟인 3개의 갯수
        """
        nums.sort()
        
        diff = float('inf')
        answer = None
        for i in range(len(nums)-2):
            l, r = i+1, len(nums)-1
            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]

                if three_sum == target:
                    return target
                else:
                    curr_diff = abs(three_sum - target)
                    if curr_diff < diff:
                        diff = curr_diff
                        answer = three_sum

                    if three_sum < target:
                        l += 1
                    else:
                        r -= 1
                
        return answer
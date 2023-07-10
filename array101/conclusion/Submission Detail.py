class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        nums의 갯수만큼의 리스트중에 리스트에 없는 수 반환
        Example 1:

        Input: nums = [4,3,2,7,8,2,3,1]
        Output: [5,6]
        
        n == nums.length
        1 <= n <= 105
        1 <= nums[i] <= n
        
        인풋 배열 정렬
        배열 길이만큼 반복
        해당 번호에 없으면 값 저장
        O(n)
        """
        result_list = []
        seted_nums = set(nums)
        
        
        for i in range(len(nums)):
            if i+1 not in seted_nums:
                result_list.append(i+1)
        
        return result_list
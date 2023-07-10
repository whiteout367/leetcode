class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        """
        3번째로 큰수 찾기, 없으면 가장 큰수
        Input: nums = [3,2,1]
        Output: 1
        Explanation:
        The first distinct maximum is 3.
        The second distinct maximum is 2.
        The third distinct maximum is 1.
        """
        result_list = []
        for num in nums:
            if num not in result_list:
                result_list.append(num)
        
        
        result_list.sort()
        result_list = result_list[::-1]
        
        
        if len(result_list) >= 3:
            
            return result_list[2]
        else:
            
            return result_list[0]
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        """
        Input: heights = [1,1,4,2,1,3]
        Output: 3
        Explanation: 
        heights:  [1,1,4,2,1,3]
        expected: [1,1,1,2,3,4]
        Indices 2, 4, and 5 do not match.
        
        1 <= heights.length <= 100
        1 <= heights[i] <= 100
        
        입력된 값과 정렬된 값이 일치하지 않는 갯수
        """
        
        result = 0
        
        sort_height = sorted(heights)
        
        for i in range(len(heights)):
            if sort_height[i] != height:
                result += 1
                
        return result
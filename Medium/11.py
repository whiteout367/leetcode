class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        투 포인터 기법을 사용

        값의 최소값을 찾으며 계속 반복
        """
        left=0
        right=len(height)-1
        max_area=0
        while (right-left>0) :
            max_area=max(max_area,(right-left)*min(height[left],height[right]))
                
            if height[left]>=height[right]:
                right-=1
            else:
                left+=1
            
        return max_area
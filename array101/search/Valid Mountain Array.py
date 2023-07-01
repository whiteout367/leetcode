class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        #i를 기준으로 작거나 같아야 한다.
        #i를 찾아야 한다
        #i가 길이보다 작아야 함
        #i가 큰곳
        if len(arr) < 3: return False
        
        result = False
        i = 0
        
        while i < len(arr) - 1 and arr[i] < arr[i+1]:
            i += 1
            if i ==len(arr) - 1: 
                break

        while 0 < i < len(arr) - 1 and arr[i] > arr[i+1]:
            i += 1
            if i == len(arr) - 1:
                result = True
                break
        return result
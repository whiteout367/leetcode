class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        #해당 인덱스 제외 오른쪽의 가장 큰것 나오기
        #없으면 -1 대체
        #시간 초과
        
        result_list = []
        if len(arr) == 1:
            result_list.append(-1)
            return result_list
        print(len(arr))
        l_max_index = arr.index(max(arr[1:]))
        for i in range(len(arr)):
            
            if i != len(arr) - 1:
                if i == l_max_index:
                    l_max_index = arr.index(max(arr[i+1:]))
                    
                elif i > l_max_index:
                    l_max_index = l_max_index = arr.index(max(arr[i+1:]), i)
                l_max = arr[l_max_index]
            else:
                l_max = -1
            result_list.append(l_max)
            
        return result_list
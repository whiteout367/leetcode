class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        result_list = []
        for i in range(len(arr)):
            print(arr[i])
            if arr[i] == 0:
                result_list.append(arr[i])
            result_list.append(arr[i])
        result = result_list[:len(arr)]

        for x in range(len(result)):
            arr[x] = result[x]
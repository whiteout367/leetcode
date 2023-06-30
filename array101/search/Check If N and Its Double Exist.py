class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        i = 0
        j = 1
        result = False

        while i != len(arr) - 1:
            if j != len(arr):
                if arr[i] == arr[j] * 2 or arr[i] * 2 == arr[j]:
                    result = True
                    break
                else:
                    j += 1

            else:
                i += 1
                j = i+1

        return result
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        n_num1 = []
        n_num2 = []
        for i in nums1[:m]:
            n_num1.append(i)
        for j in nums2:
            n_num1.append(j)
        s_list = sorted(n_num1 + n_num2)
        for x in range(n+m):
            nums1[x] = s_list[x]
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        two point
        1. 리스트에서 값 하나씩 가져오기
        2. 다음부터 투포인터 사용
        3. 끝에서 마지막까지

        결국 강의 들음
        1. 리스트 정렬(중복되는 값을 2번 하는 것을 피하기 위해)
        2. 반복문으로 맨 처음 값 반복
        3. 나머지 2개를 투포인터로 구함

        fail
        """
        results = []
        nums.sort()

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while left < right:
                sum = nums[i] + nums[left] + nums[right]

                if sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    results.append([nums[i], nums[left], nums[right]])

                    # 중복 제거
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return results

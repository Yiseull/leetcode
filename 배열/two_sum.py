from typing import List

class Solution:
    # first solution: 'Brute-Force' is inefficient
    # 시간복잡도: O(n^2), Runtime: 5366ms
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j] == target):
                    return [i, j]

    # second solution: in을 이용한 탐색
    # 시간복잡도: O(n^2), Runtime: 665ms
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            complement = target - n
            if complement in nums[i + 1]:
                return [i, nums[i+1:].index(complement) + (i + 1)]

    # third solution: 첫 번째 수를 뺀 결과 키 조회 (딕셔너리 사용)
    # 시간복잡도: O(n), Runtime: 96ms
    def twoSum3(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        # 키와 값을 바꿔서 딕셔너리로 저장
        for i, num in enumerate(nums):
            nums_map[num] = i
        # 타켓에서 첫 번째 수를 뺀 결과를 키로 조회
        for i, num in enumerate(nums):
            complement = target - num
            if complement in nums_map and i != nums_map[complement]:
                return [i, nums_map[complement]]

    # fourth solution: third solution 구조 개선
    # 시간복잡도: O(n), Runtime: 114ms
    def twoSum4(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target - num], i]
            nums_map[num] = i

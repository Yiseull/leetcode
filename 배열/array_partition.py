class Solution:
    # first solution
    # 시간복잡도: O(nlogn), Runtime: 345ms
    def arrayPairSum(self, nums: List[int]) -> int:
        result = 0
        nums.sort()

        for i in range(len(nums) // 2):
            # 정렬된 두 수에서 더 작은 수는 왼쪽에 놓여진 수
            result += nums[2 * i]

        return result

    # second solution: 파이썬다운 방식
    # 시간복잡도: O(nlogn), Runtime: 385ms
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])
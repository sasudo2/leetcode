class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        value = 1
        nums = set(nums)
        while value in nums:
            value += 1
        return value

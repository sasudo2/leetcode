class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        value = 1
        nums_set = set(nums)
        while value in nums_set:
            value += 1
        return value

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        while j < len(nums):
            while j < len(nums) and nums[i] == nums[j] :
                nums.pop(j)
            i += 1
            j += 1
        return len(nums)
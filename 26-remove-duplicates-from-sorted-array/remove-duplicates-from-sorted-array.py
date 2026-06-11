class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        l = len(nums)
        while j < l:
            while j < l and nums[i] == nums[j] :
                nums.pop(j)
                l -= 1
            i += 1
            j += 1
        return l
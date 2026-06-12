class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p1 = 0
        p2 = 0
        l = len(nums)
        
        while p2 < l:
            if nums[p2] == val:
                p2 += 1
            else:
                p1 += 1
                p2 += 1
            if p2 < l:
                nums[p1] = nums[p2]

        return p1 + 1 if p1 == p2 else p1
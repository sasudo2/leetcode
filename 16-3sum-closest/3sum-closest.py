class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = None
        difference = None
        nums.sort()
        length = len(nums)
        for i in range(length):
            a = nums[i]
            left = i+1
            right = length-1
            while left < right:
                b = nums[left]
                c = nums[right]
                sum = a+b+c
                if closest == None or abs(sum-target)<difference:
                    closest = sum
                    difference = abs(sum-target)

                if sum < target:
                    left += 1
                else:
                    right -= 1
        
        return closest
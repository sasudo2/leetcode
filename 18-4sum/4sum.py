class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        outputs = []
        nums.sort()
        p1 = 0
        p2 = 1
        l = 2
        r = len(nums) - 1
        while p1 <= len(nums)-4:
            while p2 <= len(nums)-3:
                while l<r:
                    if nums[p1]+nums[p2]+nums[l]+nums[r]==target:
                        outputs.append([nums[p1], nums[p2], nums[l], nums[r]])
                        l += 1
                        while l<r and nums[l] == nums[l-1]:
                            l += 1
                    elif nums[p1]+nums[p2]+nums[l]+nums[r]>target:
                        r -= 1
                    else:
                        l += 1
                p2 += 1
                while p2 <= len(nums)-3 and nums[p2] == nums[p2-1]:
                    p2 += 1
                l = p2 +1
                r = len(nums) - 1
            p1+=1
            while p1 <= len(nums)-4 and nums[p1] == nums[p1-1]:
                p1+=1
            p2 = p1 + 1
            l = p2 + 1
            r = len(nums)-1

        
        return outputs
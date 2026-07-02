class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        n = length-1

        if length == 1:
            return

        #compare form last element if nums[n-1] > nums[n]
        while nums[n] <= nums[n-1]:
            n -= 1
            if n == 0:
                nums.reverse()
                return

        pivot = n-1
        y = None
        #compare from pivot to last element if pivot < nums[n]
        while nums[pivot] < nums[n]:
            # if reached last element the last element is the y
            if n + 1 == length:
                y = n
                break
            n += 1
        
        #if reached an element for which nums[pivot] < nums[n] doesn't hold and y hasn't been assigned
        if y == None:
            y = n - 1

        #swap nums[pivot] and nums[last]
        nums[pivot], nums[y] = nums[y], nums[pivot]

        #reverse frm pivot to last element
        n = length-1
        i = 1
        while pivot + i < n - i + 1:
            nums[pivot + i], nums[n - i + 1] =  nums[n - i + 1], nums[pivot + i]
            i += 1
            
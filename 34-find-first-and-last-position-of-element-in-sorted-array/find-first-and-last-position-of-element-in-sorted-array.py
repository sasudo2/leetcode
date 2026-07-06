class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        indices = []
        found = False
        for index, num in enumerate(nums):
            if num == target:
                found = True
                indices.append(index)
            if found == True and num != target:
                break

        if found:
            return [indices[0], indices[-1]]
        else:
            return [-1, -1]
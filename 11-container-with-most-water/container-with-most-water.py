class Solution:
    def maxArea(self, height: list[int]) -> int:
        area = 0
        i = 0
        j = len(height) - 1
        while True:
            if i == j:
                break
            a = (j-i)*min(height[i], height[j])
            if a > area:
                area = a
            if height[i] > height[j]:
                j = j-1
            else:
                i = i+1
        return area
                
                
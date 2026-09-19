class Solution:
    def trap(self, height: list[int]) -> int:
        if sorted(height, reverse = True) == height:
            return 0
        volume = 0
        i = 0
        length = len(height)
        while i < length-1:
            j = i+1
            while height[i]>height[j]:
                j += 1
                if j == length:
                    if i != length - 2:
                        j = i+height[i+1:j].index(max(height[i+1:j]))+1
                        break
                    else:
                        j=i+1
                        break
            if j == i+1:
                i = j
                continue
            volume += min(height[i], height[j])*(j-i-1)-sum(height[i+1:j])
            i = j

        return volume


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_list = []
        while len(nums2) != 0 or len(nums1) != 0:
            if len(nums1) != 0 and len(nums2) != 0:
                if nums1[0] < nums2[0]:
                    merged_list.append(nums1.pop(0))
                else:
                    merged_list.append(nums2.pop(0))
            elif len(nums1) == 0:
                merged_list = merged_list + nums2
                nums2 = []
            else:
                merged_list = merged_list + nums1
                nums1 = []

        median_position = (float(len(merged_list))+1.0)/float(2)
        median = 0
        if (median_position - round(median_position, 0)) == 0:
            median = float(merged_list[int(median_position-1)])
        else:
            median = (float(merged_list[int(median_position - 0.5)]) + float(merged_list[int(median_position - 1.5)]))/2.0
        
        return median
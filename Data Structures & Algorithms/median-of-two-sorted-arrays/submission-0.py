class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1) + len(nums2)
        if n == 0:
            return 0.0

        merge = []
        x = y = i = 0

        while x < len(nums1) and y < len(nums2) and len(merge) < (n//2) + 1:
            if nums1[x] <= nums2[y]:
                merge.append(nums1[x])
                x += 1
                i += 1
            else:
                merge.append(nums2[y])
                y += 1
                i += 1

        while x < len(nums1) and len(merge) < (n//2) + 1:
            merge.append(nums1[x])
            x += 1
        while y < len(nums2) and len(merge) < (n//2) + 1:
            merge.append(nums2[y])
            y += 1
        
        if n % 2 == 0:
            return (merge[len(merge) - 1] + merge[len(merge) - 2]) / 2.0
        else:
            return float(merge[len(merge) - 1])

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l = 0
        h = len(nums) - 1
        while l <= h:
            m = (l + h) // 2
            if m == 0 and nums[m + 1] < nums[m]:
                return nums[m + 1]
            elif nums[m] < nums[m - 1]:
                return nums[m]
            elif nums[m] > nums[h]:
                l = m + 1
            else:
                h = m - 1
        # lowest = min(nums[len(nums) - 1], nums[0])
        # while l <= h:
        #     mid = (l + h) // 2
        #     if mid == 0 and nums[mid + 1] < nums[mid]:
        #         return nums[mid + 1] 
        #     elif nums[mid] < nums[mid - 1]:
        #         return nums[mid]
        #     elif nums[mid] < lowest:
        #         lowest = nums[mid]
        #         h = mid - 1
        #     else:
        #         l = mid + 1
        return nums[0]
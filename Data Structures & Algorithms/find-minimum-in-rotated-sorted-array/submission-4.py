class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l = 0
        h = len(nums) - 1
        lowest = min(nums[len(nums) - 1], nums[0])
        while l <= h:
            mid = (l + h) // 2
            if mid == 0 and nums[mid + 1] < nums[mid]:
                return nums[mid + 1] 
            elif nums[mid] < nums[mid - 1]:
                return nums[mid]
            elif nums[mid] < lowest:
                lowest = nums[mid]
                h = mid - 1
            else:
                l = mid + 1
        return nums[0]
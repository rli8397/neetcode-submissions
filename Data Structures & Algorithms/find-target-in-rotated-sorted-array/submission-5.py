class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        
        #finds pivot point
        pivot = 0
        l = 0
        h = len(nums) - 1
        lowest = min(nums[len(nums) - 1], nums[0])
        while l <= h:
            mid = (l + h) // 2
            if mid == 0 and nums[mid + 1] < nums[mid]:
                pivot = mid + 1
                break
            elif nums[mid] < nums[mid - 1]:
                pivot = mid
                break
            elif nums[mid] < lowest:
                lowest = nums[mid]
                h = mid - 1
            else:
                l = mid + 1

        print(pivot)

        # first half
        l = 0
        h = pivot - 1
        while l <= h:
            m = (l + h) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                h = m - 1
        
        l = pivot
        h = len(nums) - 1
        while l <= h:
            m = (l + h) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                h = m - 1
                
        return -1
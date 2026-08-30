class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(nums[i] * prefix[len(prefix) - 1])
        
        postfix = [0] * len(nums)
        postfix[len(nums) - 1] = nums[len(nums) - 1]
        for i in range(len(nums) - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i]
        
        print(prefix, postfix)

        res = [postfix[1]] 
        for i in range(1, len(nums) - 1):
            res.append(prefix[i - 1] * postfix[i + 1])
        res.append(prefix[len(prefix) - 2])

        return res
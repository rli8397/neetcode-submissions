class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.backtrack(nums)
    def backtrack(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        output = []
        for i in range(len(nums)):
            starts_with_i = []
            permute_rest = self.backtrack(nums[:i] + nums[i+1:])
            for arr in permute_rest:
                starts_with_i.append([nums[i]] + arr)
            output += starts_with_i
        return output

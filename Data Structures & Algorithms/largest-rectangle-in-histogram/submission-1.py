class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        stack = []

        for i in range(len(heights)):
            left = i
            while stack and stack[-1][0] >= heights[i]:
                curr = stack.pop() # stack[0] = height; stack[1] = index
                ans = max(ans, curr[0] * (i - curr[1]))
                left = curr[1]
            stack.append((heights[i], left))

        for h, i in stack:
            ans = max(ans, h * (len(heights) - i))

        return ans

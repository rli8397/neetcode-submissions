class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        end = False
        stack = []
        stack.append([temperatures[len(temperatures) - 1], len(temperatures) -1])

        for i in reversed(range(len(temperatures)-1)):
            if temperatures[i] < stack[len(stack)-1][0]:
                ans[i] = 1
            else: 
                print(stack)
                while len(stack) >= 1 and temperatures[i] >= stack[len(stack) - 1][0]:
                    stack.pop()
                if len(stack) == 0:
                    ans[i] = 0
                else:
                    ans[i] = stack[len(stack) - 1][1] - i
            stack.append([temperatures[i], i])



        return ans
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        ans = int(tokens[0])
        operators = set(["+", "-", "*", "/"])
        for i in range(len(tokens)):
            if tokens[i]  == "+": 
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                ans = num1 + num2
                stack.append(ans);
            elif tokens[i] == "-":
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                ans = num2 - num1
                stack.append(ans);
            elif tokens[i] == "*":
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                ans = num1 * num2
                stack.append(ans);
            elif tokens[i] == "/":
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                sign = 1
                ans = num2 / num1
                if ans < 0:
                    sign = -1
                ans = int(abs(ans)) * sign
                stack.append(ans);
            else:
                stack.append(tokens[i])
        return ans

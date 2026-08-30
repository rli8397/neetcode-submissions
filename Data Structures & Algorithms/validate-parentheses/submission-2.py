class Solution:
    def isValid(self, s: str) -> bool:
        arr = deque()
        opening = ["(", "[", "{"]
        closing = [")", "]", "}"]
        for i in range(len(s)):
            isClosingBracket = False
            for j in range(len(closing)):
                if s[i] == closing[j]:
                    if len(arr) > 0:
                        prev = arr.pop()
                    else:
                        return False
                    isClosingBracket = True
                    if opening[j] == prev:
                        break
                    else:
                        return False
            if not isClosingBracket: 
                arr.append(s[i])
        return len(arr) == 0
            
        
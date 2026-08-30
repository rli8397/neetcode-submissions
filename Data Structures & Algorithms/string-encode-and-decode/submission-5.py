class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for i in range(len(strs)):
            ret += "#" + str(len(strs[i])) + "#"
            for letter in strs[i]:
                ret += letter
        return ret

    def decode(self, s: str) -> List[str]:
        arr = []
        i = 1
        while i < len(s):
            length = ""
            while i < len(s) and s[i] != "#":
                length += s[i]
                i += 1
            i += 1
            length = int(length)
            currWord = ""
            for j in range(length):
                currWord += s[i]
                i += 1
            arr.append(currWord)
            i += 1 
        return arr

                      
            
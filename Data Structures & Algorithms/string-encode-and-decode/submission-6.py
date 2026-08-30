class Solution:
    def encode(self, strs: List[str]) -> str:
        coded = ""
        for s in strs:
            curr = ""
            for i in range(len(s)):
                curr += chr((ord(s[i]) + 10) % 127)
            coded += curr + "#"
        return coded

    def decode(self, s: str) -> List[str]:
        decoded = []
        coded = ""
        for i in s:
            if i == "#":
                decoded.append(coded)
                coded = ""
            else:
                char = ord(i) - 10 
                if char < 0:
                    char += 127
                coded += chr(char)
        return decoded
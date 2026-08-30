class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        l = 0
        freqS1 = [0] * 26
        freqS2 = [0] * 26
        for i in range(len(s1)):
            freqS1[ord(s1[i]) - 97] += 1
            freqS2[ord(s2[i]) - 97] += 1
        print(freqS1)

        difference = 0
        for i in range(26):
            difference += abs(freqS1[i] - freqS2[i])
            # if freqS1[i] != freqS2[i]:
            #     difference += freq
        
        if difference == 0:
            return True
        
        while l + len(s1) < len(s2):
            prevStr = ord(s2[l]) - 97 
            if freqS1[prevStr] < freqS2[prevStr]:
                difference -= 1
            else:
                difference += 1
            freqS2[prevStr] -= 1
            
            print(difference, freqS2)
            l += 1
            currStr = ord(s2[l + len(s1) - 1]) - 97
            if freqS1[currStr] > freqS2[currStr]:
                difference -= 1
            else: 
                difference += 1
            freqS2[currStr] += 1
            print(l, difference, freqS2)
            if difference == 0:
                return True

        return difference == 0
            
            
            




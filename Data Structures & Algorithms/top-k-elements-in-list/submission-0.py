class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {} 

        highestFreq = 0
        for i in nums:
            if i not in d:
                d[i] = 0
            d[i] += 1
            highestFreq = max(highestFreq, d[i])
        
        freq = [[] for _ in range(highestFreq + 1)]
        for key in d.keys():
            freq[d[key]].append(key)
        
        res = [] 
        for i in range(len(freq) - 1, -1, -1):
            print(freq[i])
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res

        return res

            
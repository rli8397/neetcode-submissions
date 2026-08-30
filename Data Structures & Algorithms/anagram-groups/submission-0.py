class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        res = []
        i = 0
        for j in strs:
            k = "".join(sorted(j))
            print(k)
            if k in d:
                res[d[k]].append(j)
            else:
                d[k] = i
                res.append([j])
                i += 1
        return res


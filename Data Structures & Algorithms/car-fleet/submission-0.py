class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sortedlist = []
        for i in range(len(position)):
            sortedlist.append([position[i], speed[i]])
        
        sortedlist.sort(key=lambda point: point[0])
        prev = -1
        ans = 0
        for i in reversed(range(len(position))):
            curr = (target - sortedlist[i][0]) / sortedlist[i][1]
            if prev < curr:
                ans += 1
                prev = curr

        return ans




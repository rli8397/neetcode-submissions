class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        negateNums = [-x for x in nums]
        out = []
        for i in range(k):
            heapq.heappush(heap, (negateNums[i], i))
        out.append(heap[0][0] * -1)
        for i in range(k, len(nums)):
            heapq.heappush(heap, (negateNums[i], i))
            while len(heap) > 0 and heap[0][1] <= i - k:
                heapq.heappop(heap)
            out.append(heap[0][0] * -1)
        return out
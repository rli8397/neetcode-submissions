class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))
        out = [heap[0][0] * -1]

        for i in range(k, len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            while len(heap) > 0 and heap[0][1] <= i - k:
                heapq.heappop(heap)
            out.append(heap[0][0] * -1)
        return out
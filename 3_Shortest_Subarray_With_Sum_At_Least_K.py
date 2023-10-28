from collections import deque
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        dq = deque([0, 0])
        result, curr = float('inf'), 0

        for i, a in enumerate(nums):
            curr += a
            while dq and curr - dq[0][1] >= k:

                result = min(result, i + 1 - dq.popleft()[0])
            while dq and curr <= dq[-1][1]:
                dq.pop()
            dq.append([i + 1, curr])
            
        if result < float('inf'):
            return result
        else:
            return -1

# from heapq import heapify, heappop, heappush
from typing import List
import heapq
import collections


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        heapq.heapify(list(counter.values()))

        return heapq.nlargest(k, counter.keys(), key=counter.get)
        # counter = collections.Counter(nums)        
        # out = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        # return [out[i][0] for i in range(0, k)]
        
        
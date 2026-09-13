from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        ans = []
        for i in range(k):
            max_val = max(freq, key=freq.get)
            ans.append(max_val)
            freq.pop(max_val, None)
        return ans
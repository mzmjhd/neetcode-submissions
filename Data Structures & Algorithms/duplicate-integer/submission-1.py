from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums)
        print (count)
        for x in count.values():
            print(x)
            if x > 1:
                return True
        return False
        
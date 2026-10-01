class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_c = 0
        if nums == []:
            return 0
        #strip duplicates
        ls = set(nums)
        for k in ls:
            if k-1 not in ls:
                #loop to add numbers in array
                c = 0
                x = k
                while (x in ls):
                    c += 1
                    x += 1
                if c > max_c:
                    max_c = c
            else:
                continue
        return max_c
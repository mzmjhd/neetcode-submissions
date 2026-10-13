class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        summ = nums[0]
        curSum = 0
        for r in range(len(nums)):
            if curSum < 0:
                curSum = 0
            curSum += nums[r]
            summ = max(summ,curSum)
        return summ
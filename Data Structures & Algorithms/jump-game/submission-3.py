class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        if nums[0] == 0:
            return False
        maxI = 0
        for i in range(len(nums)-1):
            if i > maxI:
                return False
            maxI = max(maxI, i+nums[i])
            if maxI >= len(nums)-1:
                return True
        return False